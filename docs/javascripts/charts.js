// Interactive price charts for ```chart fences, drawn with TradingView
// Lightweight Charts (docs/assets/vendor/lightweight-charts, Apache-2.0).
//
// A fence looks like this (one "key: value" per line; see LESSON_TEMPLATE.md):
//
//   ```chart
//   data: 05-reading-charts/uptrend.json
//   title: An uptrend with a pullback
//   show: volume, sma 20, sma 50, rsi 14
//   level: 104.20 | Support
//   zone: 101.5-103.0 | 2026-03-02 to 2026-03-20 | Fair value gap
//   marker: 2026-03-14 | below | Entry
//   line: 2026-02-02 96.4 to 2026-03-10 103.8 | Trendline
//   range: 2026-02-01 to 2026-04-30
//   caption: The pullback held the 20-day average.
//   ```
//
// Data files live in docs/assets/charts/ and are made by tools/make_charts.py:
//   {"tf": "D" | "5m" | ..., "synthetic": true, "bars": [[time, o, h, l, c, v], ...]}
// Daily times are "YYYY-MM-DD". Intraday times are Unix seconds that encode the
// New York (Toronto) wall clock as if it were UTC, so the axis shows ET without
// any time zone maths in the browser.
//
// The indicator functions are plain and exported for the Node tests
// (tools/test_charts.mjs).

;(function () {
  "use strict"

  // ---------- indicators (pure functions on arrays of numbers) ----------

  function sma(values, n) {
    const out = new Array(values.length).fill(null)
    let sum = 0
    for (let i = 0; i < values.length; i++) {
      sum += values[i]
      if (i >= n) sum -= values[i - n]
      if (i >= n - 1) out[i] = sum / n
    }
    return out
  }

  // EMA seeded with the SMA of the first n values (the usual charting convention).
  function ema(values, n) {
    const out = new Array(values.length).fill(null)
    if (values.length < n) return out
    const k = 2 / (n + 1)
    let prev = 0
    for (let i = 0; i < n; i++) prev += values[i]
    prev /= n
    out[n - 1] = prev
    for (let i = n; i < values.length; i++) {
      prev = values[i] * k + prev * (1 - k)
      out[i] = prev
    }
    return out
  }

  // Wilder's smoothing: seed with the simple average of the first n values.
  function wilder(values, n, start) {
    const out = new Array(values.length).fill(null)
    const first = start + n - 1
    if (values.length <= first) return out
    let prev = 0
    for (let i = start; i <= first; i++) prev += values[i]
    prev /= n
    out[first] = prev
    for (let i = first + 1; i < values.length; i++) {
      prev = (prev * (n - 1) + values[i]) / n
      out[i] = prev
    }
    return out
  }

  function rsi(closes, n) {
    const gains = [0]
    const losses = [0]
    for (let i = 1; i < closes.length; i++) {
      const d = closes[i] - closes[i - 1]
      gains.push(Math.max(d, 0))
      losses.push(Math.max(-d, 0))
    }
    const ag = wilder(gains, n, 1)
    const al = wilder(losses, n, 1)
    return closes.map((_, i) => {
      if (ag[i] === null) return null
      if (al[i] === 0) return ag[i] === 0 ? 50 : 100
      return 100 - 100 / (1 + ag[i] / al[i])
    })
  }

  function trueRange(bars) {
    return bars.map((b, i) => {
      if (i === 0) return b.high - b.low
      const pc = bars[i - 1].close
      return Math.max(b.high - b.low, Math.abs(b.high - pc), Math.abs(b.low - pc))
    })
  }

  function atr(bars, n) {
    return wilder(trueRange(bars), n, 0)
  }

  function macd(closes, fast, slow, signal) {
    const ef = ema(closes, fast)
    const es = ema(closes, slow)
    const line = closes.map((_, i) => (ef[i] === null || es[i] === null ? null : ef[i] - es[i]))
    const startIdx = line.findIndex((v) => v !== null)
    const sig = new Array(closes.length).fill(null)
    if (startIdx >= 0) {
      const tail = ema(line.slice(startIdx), signal)
      tail.forEach((v, j) => (sig[startIdx + j] = v))
    }
    const hist = line.map((v, i) => (v === null || sig[i] === null ? null : v - sig[i]))
    return { line, signal: sig, hist }
  }

  function stdev(values, n) {
    const mean = sma(values, n)
    return values.map((_, i) => {
      if (mean[i] === null) return null
      let s = 0
      for (let j = i - n + 1; j <= i; j++) s += (values[j] - mean[i]) ** 2
      return Math.sqrt(s / n) // population standard deviation, as Bollinger used
    })
  }

  function bollinger(closes, n, k) {
    const mid = sma(closes, n)
    const sd = stdev(closes, n)
    return {
      mid,
      upper: mid.map((m, i) => (m === null ? null : m + k * sd[i])),
      lower: mid.map((m, i) => (m === null ? null : m - k * sd[i])),
    }
  }

  function keltner(bars, n, k) {
    const mid = ema(bars.map((b) => b.close), n)
    const a = atr(bars, n)
    return {
      mid,
      upper: mid.map((m, i) => (m === null || a[i] === null ? null : m + k * a[i])),
      lower: mid.map((m, i) => (m === null || a[i] === null ? null : m - k * a[i])),
    }
  }

  // Slow stochastic: %K = SMA(raw %K, smooth), %D = SMA(%K, d).
  function stoch(bars, n, smooth, d) {
    const raw = bars.map((b, i) => {
      if (i < n - 1) return null
      let hi = -Infinity
      let lo = Infinity
      for (let j = i - n + 1; j <= i; j++) {
        hi = Math.max(hi, bars[j].high)
        lo = Math.min(lo, bars[j].low)
      }
      return hi === lo ? 50 : (100 * (b.close - lo)) / (hi - lo)
    })
    const smoothNull = (arr, m) => {
      const start = arr.findIndex((v) => v !== null)
      const out = new Array(arr.length).fill(null)
      if (start < 0) return out
      sma(arr.slice(start), m).forEach((v, j) => (out[start + j] = v))
      return out
    }
    const k = smoothNull(raw, smooth)
    return { k, d: smoothNull(k, d) }
  }

  // VWAP with the typical price (high + low + close) / 3. It restarts at each
  // new session (a new date) for intraday data, or at the anchor index.
  function vwap(bars, anchor, intraday) {
    let pv = 0
    let vol = 0
    let day = null
    return bars.map((b, i) => {
      if (i < anchor) return null
      const d = intraday ? new Date(b.time * 1000).toISOString().slice(0, 10) : null
      if (intraday && d !== day) {
        pv = 0
        vol = 0
        day = d
      }
      const tp = (b.high + b.low + b.close) / 3
      pv += tp * b.volume
      vol += b.volume
      return vol ? pv / vol : null
    })
  }

  const ind = { sma, ema, rsi, atr, macd, bollinger, keltner, stoch, vwap, trueRange, stdev }

  // ---------- the fence spec ----------

  function parseSpec(text) {
    const spec = { show: [], levels: [], zones: [], markers: [], lines: [], height: 360 }
    for (const raw of text.split(/\r?\n/)) {
      const line = raw.trim()
      if (!line || line.startsWith("#")) continue
      const m = /^([a-z]+):\s*(.*)$/.exec(line)
      if (!m) continue
      const key = m[1]
      const val = m[2].trim()
      const parts = val.split("|").map((s) => s.trim())
      if (key === "data" || key === "title" || key === "caption" || key === "type") spec[key] = val
      else if (key === "height") spec.height = Math.max(200, Math.min(700, Number(val) || 360))
      else if (key === "show") spec.show = val.split(",").map((s) => s.trim().split(/\s+/)).filter((a) => a[0])
      else if (key === "level") spec.levels.push({ price: Number(parts[0]), label: parts[1] || "" })
      else if (key === "zone") {
        const [lo, hi] = parts[0].split(/\s*-\s*(?=\d)/).map(Number)
        let from = null
        let to = null
        let label = parts[1] || ""
        if (parts.length >= 3 || / to /.test(parts[1] || "")) {
          const span = (parts[1] || "").split(/\s+to\s+/)
          if (span.length === 2) {
            from = span[0]
            to = span[1]
            label = parts[2] || ""
          }
        }
        spec.zones.push({ low: Math.min(lo, hi), high: Math.max(lo, hi), from, to, label })
      } else if (key === "marker") {
        spec.markers.push({ time: parts[0], position: parts[1] === "above" ? "above" : "below", text: parts[2] || "" })
      } else if (key === "line") {
        const mm = /^(\S+(?: \d\d:\d\d)?)\s+([\d.]+)\s+to\s+(\S+(?: \d\d:\d\d)?)\s+([\d.]+)$/.exec(parts[0])
        if (mm) spec.lines.push({ t1: mm[1], p1: Number(mm[2]), t2: mm[3], p2: Number(mm[4]), label: parts[1] || "" })
      } else if (key === "range") {
        const span = val.split(/\s+to\s+/)
        if (span.length === 2) spec.range = { from: span[0], to: span[1] }
      }
    }
    return spec
  }

  // Bars from the compact file format.
  function toBars(data) {
    return data.bars.map((r) => ({ time: r[0], open: r[1], high: r[2], low: r[3], close: r[4], volume: r[5] || 0 }))
  }

  // A time written in a fence, as the chart's time value.
  function parseTime(text, intraday, firstTime) {
    if (!intraday) return text
    let date
    let clock
    if (/^\d\d:\d\d$/.test(text)) {
      date = new Date(firstTime * 1000).toISOString().slice(0, 10)
      clock = text
    } else {
      ;[date, clock] = text.split(" ")
    }
    return Date.parse(`${date}T${clock || "00:00"}:00Z`) / 1000
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { ind, parseSpec, toBars, parseTime }
  }
  if (typeof window === "undefined" || typeof document === "undefined") return

  // ---------- drawing ----------

  const SITE_ROOT = (function () {
    try {
      const s = document.currentScript && document.currentScript.src
      if (s) return new URL("../", s).href
    } catch (e) {
      /* fall through */
    }
    return null
  })()

  function siteRoot() {
    if (SITE_ROOT) return SITE_ROOT
    try {
      const cfg = JSON.parse(document.getElementById("__config").textContent)
      return new URL(cfg.base.replace(/\/?$/, "/"), location.href).href
    } catch (e) {
      return new URL("/", location.href).href
    }
  }

  const cache = new Map()
  function loadData(path) {
    if (!cache.has(path)) {
      const url = new URL("assets/charts/" + path, siteRoot()).href
      cache.set(
        path,
        fetch(url).then((r) => {
          if (!r.ok) throw new Error(`${r.status} for ${path}`)
          return r.json()
        })
      )
    }
    return cache.get(path)
  }

  function palette() {
    const cs = getComputedStyle(document.body)
    const v = (name, fallback) => (cs.getPropertyValue(name) || "").trim() || fallback
    return {
      bg: v("--tw-chart-bg", "#0e1116"),
      fg: v("--tw-chart-fg", "#c9d1d9"),
      grid: v("--tw-chart-grid", "#1f252d"),
      up: v("--tw-up", "#2fbf71"),
      down: v("--tw-down", "#e5534b"),
      accent: v("--tw-accent", "#f0a020"),
      s: [v("--tw-s1", "#f0a020"), v("--tw-s2", "#58a6ff"), v("--tw-s3", "#d2a8ff"), v("--tw-s4", "#7ee0c0"), v("--tw-s5", "#ff9e7a")],
      zone: v("--tw-chart-zone", "rgba(240,160,32,0.16)"),
      font: v("--tw-chart-font", "'IBM Plex Mono', ui-monospace, monospace"),
    }
  }

  function chartOptions(p, intraday) {
    return {
      autoSize: true,
      layout: {
        background: { type: "solid", color: p.bg },
        textColor: p.fg,
        fontFamily: p.font,
        fontSize: 11,
        attributionLogo: true,
        panes: { separatorColor: p.grid, enableResize: false },
      },
      grid: { vertLines: { color: p.grid }, horzLines: { color: p.grid } },
      rightPriceScale: { borderColor: p.grid },
      timeScale: { borderColor: p.grid, timeVisible: intraday, secondsVisible: false },
      crosshair: { mode: LightweightCharts.CrosshairMode.Normal },
      handleScale: { mouseWheel: false },
      handleScroll: { mouseWheel: false },
    }
  }

  const live = new Set()

  // A rectangle between two prices, over a time span or the whole chart.
  class Zone {
    constructor(z, color) {
      this.z = z
      this.color = color
    }
    attached({ chart, series }) {
      this.chart = chart
      this.series = series
    }
    updateAllViews() {}
    paneViews() {
      const self = this
      return [
        {
          zOrder: () => "bottom",
          renderer: () => ({
            draw: () => {},
            drawBackground(target) {
              const s = self.series
              const ts = self.chart.timeScale()
              const y1 = s.priceToCoordinate(self.z.high)
              const y2 = s.priceToCoordinate(self.z.low)
              if (y1 === null || y2 === null) return
              target.useMediaCoordinateSpace(({ context, mediaSize }) => {
                let x1 = 0
                let x2 = mediaSize.width
                if (self.z.fromT !== undefined && self.z.fromT !== null) {
                  const a = ts.timeToCoordinate(self.z.fromT)
                  const b = ts.timeToCoordinate(self.z.toT)
                  if (a === null || b === null) return
                  x1 = a
                  x2 = b
                }
                context.fillStyle = self.color
                context.fillRect(x1, y1, x2 - x1, y2 - y1)
              })
            },
          }),
        },
      ]
    }
  }

  // Draw a chart into el. Returns a handle the drills use.
  function render(el, spec, data) {
    const L = LightweightCharts
    const bars = toBars(data)
    const intraday = data.tf !== "D" && data.tf !== "W"
    const p = palette()
    el.innerHTML = ""
    const box = document.createElement("div")
    box.className = "tw-chart-box"
    el.appendChild(box)
    const panes = spec.show.filter((s) => ["rsi", "macd", "atr", "stoch"].includes(s[0])).length
    box.style.height = spec.height + panes * 110 + "px"

    const chart = L.createChart(box, chartOptions(p, intraday))
    const time = (t) => parseTime(t, intraday, bars[0].time)
    let main
    if (spec.type === "line") {
      main = chart.addSeries(L.LineSeries, { color: p.s[1], lineWidth: 2, priceLineVisible: false })
      main.setData(bars.map((b) => ({ time: b.time, value: b.close })))
    } else if (spec.type === "bar") {
      main = chart.addSeries(L.BarSeries, { upColor: p.up, downColor: p.down, priceLineVisible: false })
      main.setData(bars)
    } else {
      main = chart.addSeries(L.CandlestickSeries, {
        upColor: p.up,
        downColor: p.down,
        borderVisible: false,
        wickUpColor: p.up,
        wickDownColor: p.down,
        priceLineVisible: false,
      })
      main.setData(bars)
    }

    const closes = bars.map((b) => b.close)
    const lineOpts = (color, width) => ({
      color,
      lineWidth: width || 1,
      priceLineVisible: false,
      lastValueVisible: false,
      crosshairMarkerVisible: false,
    })
    const put = (series, values) =>
      series.setData(bars.map((b, i) => (values[i] === null ? { time: b.time } : { time: b.time, value: values[i] })))
    let colour = 0
    const next = () => p.s[colour++ % p.s.length]
    let pane = 0
    const legend = []

    for (const item of spec.show) {
      const [name, a, b, c] = item
      const n = (x, d) => (x === undefined ? d : Number(x))
      if (name === "volume") {
        const vol = chart.addSeries(L.HistogramSeries, { priceFormat: { type: "volume" }, priceScaleId: "", lastValueVisible: false, priceLineVisible: false })
        vol.priceScale().applyOptions({ scaleMargins: { top: 0.82, bottom: 0 } })
        vol.setData(bars.map((b) => ({ time: b.time, value: b.volume, color: b.close >= b.open ? p.up + "66" : p.down + "66" })))
      } else if (name === "sma" || name === "ema") {
        const len = n(a, 20)
        const col = next()
        put(chart.addSeries(L.LineSeries, lineOpts(col, 2)), ind[name](closes, len))
        legend.push([col, `${name.toUpperCase()} ${len}`])
      } else if (name === "vwap" || name === "avwap") {
        let anchor = 0
        if (name === "avwap" && a) {
          const t = time(item.slice(1).join(" "))
          anchor = Math.max(0, bars.findIndex((bar) => bar.time === t))
        }
        const col = p.accent
        put(chart.addSeries(L.LineSeries, lineOpts(col, 2)), vwap(bars, anchor, intraday && name === "vwap"))
        legend.push([col, name === "vwap" ? "VWAP" : "Anchored VWAP"])
      } else if (name === "bb" || name === "keltner") {
        const len = n(a, 20)
        const k = n(b, name === "bb" ? 2 : 1.5)
        const bands = name === "bb" ? bollinger(closes, len, k) : keltner(bars, len, k)
        const col = next()
        for (const key of ["upper", "mid", "lower"]) put(chart.addSeries(L.LineSeries, lineOpts(col, key === "mid" ? 1 : 1)), bands[key])
        legend.push([col, `${name === "bb" ? "Bollinger" : "Keltner"} ${len}, ${k}`])
      } else if (name === "rsi") {
        pane += 1
        const len = n(a, 14)
        const s = chart.addSeries(L.LineSeries, lineOpts(p.s[1], 2), pane)
        put(s, rsi(closes, len))
        for (const lv of [30, 70]) s.createPriceLine({ price: lv, color: p.fg + "88", lineWidth: 1, lineStyle: L.LineStyle.Dashed, axisLabelVisible: true, title: "" })
        legend.push([p.s[1], `RSI ${len}`])
      } else if (name === "macd") {
        pane += 1
        const m = macd(closes, n(a, 12), n(b, 26), n(c, 9))
        const h = chart.addSeries(L.HistogramSeries, { priceLineVisible: false, lastValueVisible: false }, pane)
        h.setData(bars.map((bar, i) => (m.hist[i] === null ? { time: bar.time } : { time: bar.time, value: m.hist[i], color: m.hist[i] >= 0 ? p.up + "99" : p.down + "99" })))
        put(chart.addSeries(L.LineSeries, lineOpts(p.s[1], 2), pane), m.line)
        put(chart.addSeries(L.LineSeries, lineOpts(p.accent, 1), pane), m.signal)
        legend.push([p.s[1], `MACD ${n(a, 12)}, ${n(b, 26)}, ${n(c, 9)}`])
      } else if (name === "atr") {
        pane += 1
        const len = n(a, 14)
        put(chart.addSeries(L.LineSeries, lineOpts(p.s[3], 2), pane), atr(bars, len))
        legend.push([p.s[3], `ATR ${len}`])
      } else if (name === "stoch") {
        pane += 1
        const st = stoch(bars, n(a, 14), n(b, 3), n(c, 3))
        const s = chart.addSeries(L.LineSeries, lineOpts(p.s[1], 2), pane)
        put(s, st.k)
        put(chart.addSeries(L.LineSeries, lineOpts(p.accent, 1), pane), st.d)
        for (const lv of [20, 80]) s.createPriceLine({ price: lv, color: p.fg + "88", lineWidth: 1, lineStyle: L.LineStyle.Dashed, axisLabelVisible: true, title: "" })
        legend.push([p.s[1], `Stochastic ${n(a, 14)}, ${n(b, 3)}, ${n(c, 3)}`])
      }
    }
    chart.panes().forEach((pn, i) => {
      if (i > 0) pn.setHeight(100)
    })

    for (const lv of spec.levels) {
      main.createPriceLine({ price: lv.price, color: p.accent, lineWidth: 1, lineStyle: L.LineStyle.Dashed, axisLabelVisible: true, title: lv.label })
    }
    for (const z of spec.zones) {
      const zz = Object.assign({}, z, { fromT: z.from ? time(z.from) : null, toT: z.to ? time(z.to) : null })
      main.attachPrimitive(new Zone(zz, p.zone))
      if (z.label) legend.push([p.zone, `${z.label} (${z.low} to ${z.high})`])
    }
    for (const ln of spec.lines) {
      const s = chart.addSeries(L.LineSeries, lineOpts(p.fg, 2))
      s.setData([
        { time: time(ln.t1), value: ln.p1 },
        { time: time(ln.t2), value: ln.p2 },
      ])
      if (ln.label) legend.push([p.fg, ln.label])
    }
    if (spec.markers.length) {
      const marks = spec.markers
        .map((mk) => ({
          time: time(mk.time),
          position: mk.position === "above" ? "aboveBar" : "belowBar",
          shape: mk.position === "above" ? "arrowDown" : "arrowUp",
          color: p.accent,
          text: mk.text,
        }))
        .sort((x, y) => (x.time < y.time ? -1 : x.time > y.time ? 1 : 0))
      L.createSeriesMarkers(main, marks)
    }

    if (spec.range) {
      const from = time(spec.range.from)
      const to = time(spec.range.to)
      chart.timeScale().setVisibleRange({ from, to })
    } else {
      chart.timeScale().fitContent()
    }

    if (legend.length) {
      const lg = document.createElement("div")
      lg.className = "tw-chart-legend"
      for (const [col, text] of legend) {
        const item = document.createElement("span")
        const sw = document.createElement("i")
        sw.style.background = col
        item.appendChild(sw)
        item.appendChild(document.createTextNode(text))
        lg.appendChild(item)
      }
      el.appendChild(lg)
    }

    const handle = {
      chart,
      main,
      bars,
      intraday,
      el,
      priceAt: (y) => main.coordinateToPrice(y),
      restyle() {
        const q = palette()
        chart.applyOptions(chartOptions(q, intraday))
      },
      remove() {
        live.delete(handle)
        chart.remove()
      },
    }
    live.add(handle)
    return handle
  }

  function figureFor(pre, spec) {
    const fig = document.createElement("figure")
    fig.className = "tw-chart"
    if (spec.title) {
      const t = document.createElement("div")
      t.className = "tw-chart-title"
      t.textContent = spec.title
      fig.appendChild(t)
    }
    const area = document.createElement("div")
    area.className = "tw-chart-area"
    fig.appendChild(area)
    const cap = document.createElement("figcaption")
    cap.textContent = (spec.caption ? spec.caption + " " : "") + "Made-up price data, for teaching."
    fig.appendChild(cap)
    pre.replaceWith(fig)
    return area
  }

  function renderFences() {
    // Drop charts whose page has gone (instant navigation).
    for (const h of Array.from(live)) if (!document.body.contains(h.el)) h.remove()
    document.querySelectorAll("pre.chart").forEach((pre) => {
      const spec = parseSpec(pre.textContent)
      if (!spec.data) return
      const area = figureFor(pre, spec)
      loadData(spec.data)
        .then((data) => render(area, spec, data))
        .catch((err) => {
          area.textContent = "This chart could not load (" + err.message + ")."
          area.className = "tw-chart-error"
        })
    })
  }

  // Re-colour every chart when the reader switches light and dark.
  new MutationObserver(() => live.forEach((h) => h.restyle())).observe(document.body, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"],
  })

  window.TWCharts = { render, parseSpec, loadData, palette, ind }
  document$.subscribe(renderFences)
})()
