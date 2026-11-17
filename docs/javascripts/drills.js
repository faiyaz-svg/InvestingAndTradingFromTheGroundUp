// Chart drills: a card shows a chart and a question. The reader clicks the chart
// (level), types a number (number) or picks an answer (choice). A page holds
//   <div class="tw-drills" data-tool="chart-drills" data-sets="a,b"></div>
// Drill data comes from assets/drills/<set>.json (built by tools/build_drills.py).
// Progress is kept in localStorage under "itftgu-practice-v1:chart-drills".
// Pure helpers are exported for the Node tests (tools/test_drills.mjs).
;(function () {
  "use strict"

  var PREFIX = "itftgu-practice-v1"
  var TOOL = "chart-drills"
  var BOX_MAX = 4

  // ---------- numbers and grading ----------

  // "1,250.50", "$48.20", "US$48.20", " 48.2 ", "-3.5", "-$3.5" -> number, or null.
  function parseNumber(text) {
    if (typeof text === "number") return isFinite(text) ? text : null
    var s = String(text == null ? "" : text)
      .replace(/[−–]/g, "-")
      .replace(/(us|ca|c|cad|usd)?\s*\$/gi, "")
      .replace(/[\s  ]/g, "")
      .replace(/,/g, "")
    if (!/^[-+]?(\d+\.?\d*|\.\d+)$/.test(s)) return null
    var n = Number(s)
    return isFinite(n) ? n : null
  }

  // Right if the number is within tolerance (inclusive) of the answer.
  function gradeNumber(given, answer, tolerance) {
    if (typeof given !== "number" || !isFinite(given)) return false
    return Math.abs(given - answer) <= tolerance + 1e-9
  }

  // item: a drill item. given: a number (level, number) or a choice index (choice).
  function grade(item, given) {
    if (item.type === "choice") return given === item.answer_choice
    return gradeNumber(given, item.answer, item.tolerance)
  }

  function fmtPrice(n) {
    return Number(n).toFixed(2)
  }

  // ---------- Leitner queue (boxes 0 to 4) ----------

  var WEIGHTS = [16, 8, 4, 2, 1]
  var NEW_WEIGHT = 12

  // null for a card never answered.
  function boxOf(boxes, id) {
    var b = boxes ? boxes[id] : undefined
    if (typeof b !== "number" || b < 0 || b > BOX_MAX) return null
    return Math.floor(b)
  }
  function weightOf(box) {
    return box === null ? NEW_WEIGHT : WEIGHTS[box]
  }
  // A right answer moves up one box (a new card goes to box 1). A wrong one goes to box 0.
  function finish(boxes, id, right) {
    var b = boxOf(boxes, id)
    boxes[id] = right ? Math.min((b === null ? 0 : b) + 1, BOX_MAX) : 0
    return boxes
  }
  // Weighted random pick; avoids repeating the last card when there is a choice.
  function nextCard(ids, boxes, rand, avoid) {
    rand = rand || Math.random
    var pool = ids.length > 1 && avoid !== undefined ? ids.filter(function (id) { return id !== avoid }) : ids
    if (!pool.length) return undefined
    var weights = pool.map(function (id) { return weightOf(boxOf(boxes, id)) })
    var total = weights.reduce(function (a, b) { return a + b }, 0)
    var roll = rand() * total
    for (var i = 0; i < pool.length; i++) {
      roll -= weights[i]
      if (roll < 0) return pool[i]
    }
    return pool[pool.length - 1]
  }
  // A missed card is queued to return after a few more cards.
  function scheduleRetry(retry, id, asked, ids) {
    var gap = ids.length > 4 ? 3 : 1
    retry.push({ id: id, due: asked + gap })
    return retry
  }
  // The first retry that is due and still in the pool (removed from the queue), or undefined.
  function dueRetry(retry, asked, ids) {
    for (var i = 0; i < retry.length; i++) {
      if (retry[i].due <= asked) {
        var id = retry[i].id
        retry.splice(i, 1)
        if (ids.indexOf(id) >= 0) return id
        i--
      }
    }
    return undefined
  }
  function pickCard(ids, boxes, retry, asked, rand, avoid) {
    var r = dueRetry(retry, asked, ids)
    if (r !== undefined && !(ids.length > 1 && r === avoid)) return r
    if (r !== undefined) retry.unshift({ id: r, due: asked })
    return nextCard(ids, boxes, rand, avoid)
  }
  function boxCounts(ids, boxes) {
    var c = { fresh: 0, 0: 0, 1: 0, 2: 0, 3: 0, 4: 0 }
    ids.forEach(function (id) {
      var b = boxOf(boxes, id)
      if (b === null) c.fresh++
      else c[b]++
    })
    return c
  }

  var api = {
    parseNumber: parseNumber,
    gradeNumber: gradeNumber,
    grade: grade,
    fmtPrice: fmtPrice,
    boxOf: boxOf,
    weightOf: weightOf,
    finish: finish,
    nextCard: nextCard,
    scheduleRetry: scheduleRetry,
    dueRetry: dueRetry,
    pickCard: pickCard,
    boxCounts: boxCounts,
  }
  if (typeof module !== "undefined" && module.exports) module.exports = api
  if (typeof window === "undefined" || typeof document === "undefined") return

  // ---------- browser helpers ----------

  function store(name, fallback) {
    try {
      var raw = localStorage.getItem(PREFIX + ":" + name)
      return raw === null ? fallback : JSON.parse(raw)
    } catch (e) {
      return fallback
    }
  }
  function save(name, value) {
    try {
      localStorage.setItem(PREFIX + ":" + name, JSON.stringify(value))
    } catch (e) { /* storage blocked: the drill still works for this visit */ }
  }

  function h(tag, attrs, kids) {
    var el = document.createElement(tag)
    for (var k in attrs || {}) {
      var v = attrs[k]
      if (k === "text") el.textContent = v
      else if (k.indexOf("on") === 0) el.addEventListener(k.slice(2), v)
      else if (v !== false && v !== null && v !== undefined) el.setAttribute(k, v === true ? "" : v)
    }
    ;(kids || []).forEach(function (c) {
      if (c) el.appendChild(typeof c === "string" ? document.createTextNode(c) : c)
    })
    return el
  }

  // The site root, from this script's own URL (javascripts/drills.js). It stays
  // right after instant navigation, unlike the page-relative __config base.
  var SITE_ROOT = (function () {
    try {
      var s = document.currentScript && document.currentScript.src
      if (s) return new URL("../", s).href
    } catch (e) { /* fall through */ }
    return null
  })()

  function baseUrl() {
    if (SITE_ROOT) return SITE_ROOT
    try {
      var cfg = JSON.parse(document.getElementById("__config").textContent)
      return new URL(cfg.base.replace(/\/?$/, "/"), location.href).href
    } catch (e) {
      return new URL("/", location.href).href
    }
  }

  var cleanups = []
  function onCleanup(fn) {
    cleanups.push(fn)
  }

  // ---------- the tool ----------

  function run(root) {
    var names = (root.getAttribute("data-sets") || "").split(",").map(function (s) { return s.trim() }).filter(Boolean)
    var saved = store(TOOL, null) || {}
    var state = {
      boxes: saved.boxes && typeof saved.boxes === "object" ? saved.boxes : {},
      off: Array.isArray(saved.off) ? saved.off : [],
    }
    function persist() {
      save(TOOL, state)
    }

    var sets = {} // name -> items
    var byKey = {}
    var counts = { right: 0, wrong: 0 }
    var asked = 0
    var retry = []
    var lastKey
    var handle = null
    var token = 0
    var card = null // the current card context
    var dead = false

    root.textContent = ""
    var setBox = h("div", { class: "tw-d-sets", role: "group", "aria-label": "Question sets" })
    var stats = h("p", { class: "tw-d-stats", "aria-live": "off" })
    var boxLine = h("p", { class: "tw-d-boxes" })
    var reset = h("button", { type: "button", class: "tw-d-btn", text: "Reset progress" })
    var cardEl = h("div", { class: "tw-d-card" })
    root.appendChild(h("div", { class: "tw-d-top" }, [setBox, stats, boxLine, reset]))
    root.appendChild(cardEl)

    function disposeChart() {
      token++
      if (handle) {
        try { handle.remove() } catch (e) { /* already gone */ }
        handle = null
      }
    }
    onCleanup(function () {
      dead = true
      disposeChart()
      document.removeEventListener("keydown", onKey)
    })

    function activeKeys() {
      var keys = []
      names.forEach(function (n) {
        if (state.off.indexOf(n) >= 0) return
        ;(sets[n] || []).forEach(function (it) { keys.push(n + "/" + it.id) })
      })
      return keys
    }
    function boxesFor(set) {
      if (!state.boxes[set] || typeof state.boxes[set] !== "object") state.boxes[set] = {}
      return state.boxes[set]
    }
    // Flat map "set/id" -> box for the picker.
    function flatBoxes() {
      var flat = {}
      names.forEach(function (n) {
        var b = boxesFor(n)
        for (var id in b) flat[n + "/" + id] = b[id]
      })
      return flat
    }

    function paintStats() {
      var keys = activeKeys()
      var c = boxCounts(keys, flatBoxes())
      stats.textContent = "Answered " + asked + "  |  Right " + counts.right + "  |  Not quite " + counts.wrong
      boxLine.textContent = "Cards: new " + c.fresh + "  |  box 0: " + c[0] + "  |  1: " + c[1] + "  |  2: " + c[2] + "  |  3: " + c[3] + "  |  4: " + c[4]
    }

    function paintSets() {
      setBox.textContent = ""
      names.forEach(function (n) {
        var id = "tw-d-set-" + n
        var cb = h("input", { type: "checkbox", id: id })
        cb.checked = state.off.indexOf(n) < 0
        cb.addEventListener("change", function () {
          state.off = state.off.filter(function (x) { return x !== n })
          if (!cb.checked) state.off.push(n)
          persist()
          retry = []
          next()
        })
        var count = sets[n] ? " (" + sets[n].length + ")" : ""
        setBox.appendChild(h("label", { class: "tw-d-set", for: id }, [cb, h("span", { text: n + count })]))
      })
    }

    function parseCard(item, extra) {
      var text = item.chart + (extra ? "\n" + extra : "")
      return window.TWCharts.parseSpec(text)
    }

    // Draw the chart for a card. keepRange: the visible range to restore.
    function draw(ctx, extra, keepRange, after) {
      var mine = ++token
      if (handle) {
        try { handle.remove() } catch (e) { /* ignore */ }
        handle = null
      }
      var spec = parseCard(ctx.item, extra)
      if (spec.title === undefined) spec.title = ""
      window.TWCharts.loadData(spec.data)
        .then(function (data) {
          if (dead || mine !== token || !document.body.contains(ctx.chartEl)) return
          handle = window.TWCharts.render(ctx.chartEl, spec, data)
          if (keepRange) {
            try { handle.chart.timeScale().setVisibleLogicalRange(keepRange) } catch (e) { /* keep default */ }
          }
          if (after) after(handle)
        })
        .catch(function (err) {
          if (mine !== token) return
          ctx.chartEl.textContent = "This chart could not load (" + (err && err.message) + ")."
        })
    }

    function pickLine(ctx, price) {
      if (!handle) return
      if (ctx.pickLine) {
        try { handle.main.removePriceLine(ctx.pickLine) } catch (e) { /* ignore */ }
        ctx.pickLine = null
      }
      if (price === null) return
      var p = window.TWCharts.palette()
      ctx.pickLine = handle.main.createPriceLine({
        price: price,
        color: p.fg,
        lineWidth: 1,
        lineStyle: LightweightCharts.LineStyle.Dashed,
        axisLabelVisible: true,
        title: "Your pick",
      })
    }

    function feedback(ctx, right, answerText) {
      var box = ctx.feedback
      box.className = "tw-d-feedback " + (right ? "tw-d-right" : "tw-d-wrong")
      box.textContent = ""
      box.appendChild(h("strong", { text: right ? "Right." : "Not quite." }))
      box.appendChild(document.createTextNode(" Answer: " + answerText + "."))
      box.appendChild(h("p", { class: "tw-d-explain", text: ctx.item.explain }))
    }

    function answerText(item) {
      if (item.type === "choice") return item.choices[item.answer_choice]
      var s = fmtPrice(item.answer)
      return item.unit ? item.unit + s : s
    }

    // Grade the card with the value the reader gave.
    function check(ctx, given) {
      if (ctx.answered) return
      var item = ctx.item
      var right = grade(item, given)
      ctx.answered = true
      asked++
      if (right) counts.right++
      else counts.wrong++
      var key = ctx.key
      var set = ctx.set
      finish(boxesFor(set), item.id, right)
      persist()
      if (!right) scheduleRetry(retry, key, asked, activeKeys())
      paintStats()
      feedback(ctx, right, answerText(item))
      if (ctx.controls) ctx.controls.forEach(function (c) { c.disabled = true })
      if (ctx.input) ctx.input.readOnly = true
      if (ctx.buttons) {
        ctx.buttons.forEach(function (b, i) {
          b.disabled = true
          if (i === item.answer_choice) b.classList.add("tw-d-correct")
          else if (i === given) b.classList.add("tw-d-picked-wrong")
        })
      }
      ctx.next.hidden = false
      ctx.next.focus()

      // Redraw with the reveal lines, the reader's pick and the answer.
      var range = null
      if (handle) {
        try { range = handle.chart.timeScale().getVisibleLogicalRange() } catch (e) { range = null }
      }
      var pick = item.type === "level" && typeof given === "number" ? given : null
      draw(ctx, item.reveal || "", range, function (hd) {
        var p = window.TWCharts.palette()
        if (item.type === "level") {
          if (pick !== null) pickLine(ctx, pick)
          hd.main.createPriceLine({
            price: item.answer,
            color: p.accent,
            lineWidth: 2,
            lineStyle: LightweightCharts.LineStyle.Solid,
            axisLabelVisible: true,
            title: "Answer",
          })
        }
      })
    }

    function buildCard(key) {
      disposeChart()
      cardEl.textContent = ""
      var item = byKey[key].item
      var ctx = { key: key, set: byKey[key].set, item: item, answered: false, pickLine: null, pick: null }
      card = ctx
      lastKey = key

      var qid = "tw-d-q"
      cardEl.appendChild(h("p", { class: "tw-d-q", id: qid, text: item.q }))
      ctx.chartEl = h("div", { class: "tw-d-chart" })
      cardEl.appendChild(ctx.chartEl)
      ctx.feedback = h("div", { class: "tw-d-feedback", role: "status", "aria-live": "polite" })
      ctx.next = h("button", { type: "button", class: "tw-d-btn tw-d-next", text: "Next", hidden: true })
      ctx.next.addEventListener("click", next)

      if (item.type === "choice") {
        var wrap = h("div", { class: "tw-d-choices", role: "group", "aria-labelledby": qid })
        ctx.buttons = item.choices.map(function (label, i) {
          var b = h("button", { type: "button", class: "tw-d-btn tw-d-choice" }, [
            h("span", { class: "tw-d-key", text: String(i + 1) }),
            h("span", { text: label }),
          ])
          b.addEventListener("click", function () { check(ctx, i) })
          wrap.appendChild(b)
          return b
        })
        cardEl.appendChild(wrap)
      } else {
        var isLevel = item.type === "level"
        ctx.input = h("input", {
          type: "text",
          class: "tw-d-input",
          inputmode: "decimal",
          autocomplete: "off",
          spellcheck: "false",
          "aria-label": isLevel ? "Your price (click the chart or type)" : "Your answer",
          placeholder: isLevel ? "click the chart" : "number",
        })
        var go = h("button", { type: "button", class: "tw-d-btn tw-d-check", text: "Check" })
        ctx.controls = [go]
        var submit = function () {
          if (ctx.answered) return
          var n = parseNumber(ctx.input.value)
          if (n === null) {
            ctx.feedback.className = "tw-d-feedback tw-d-hint"
            ctx.feedback.textContent = isLevel ? "Click the chart to mark a price, or type one." : "Type a number first."
            return
          }
          check(ctx, n)
        }
        ctx.submit = submit
        go.addEventListener("click", submit)
        ctx.input.addEventListener("keydown", function (e) {
          if (e.key === "Enter") {
            e.preventDefault()
            submit()
          }
        })
        if (isLevel) {
          ctx.input.addEventListener("input", function () {
            if (ctx.answered) return
            pickLine(ctx, parseNumber(ctx.input.value))
          })
        }
        var row = [ctx.input]
        if (item.unit && !isLevel) row.unshift(h("span", { class: "tw-d-unit", text: item.unit }))
        row.push(go)
        cardEl.appendChild(h("div", { class: "tw-d-row" }, row))
      }
      cardEl.appendChild(ctx.feedback)
      cardEl.appendChild(ctx.next)

      draw(ctx, "", null, function (hd) {
        if (item.type !== "level") return
        hd.chart.subscribeClick(function (param) {
          if (ctx.answered || !param || !param.point) return
          if (param.paneIndex !== undefined && param.paneIndex > 0) return
          var price = hd.priceAt(param.point.y)
          if (price === null || price === undefined || !isFinite(price)) return
          ctx.input.value = fmtPrice(price)
          pickLine(ctx, Number(fmtPrice(price)))
        })
      })
      if (ctx.input && !window.matchMedia("(pointer: coarse)").matches) ctx.input.focus({ preventScroll: true })
    }

    function next() {
      var keys = activeKeys()
      if (!keys.length) {
        disposeChart()
        card = null
        cardEl.textContent = ""
        cardEl.appendChild(h("p", { class: "tw-d-note", text: Object.keys(sets).length ? "Pick at least one set above." : "No questions loaded." }))
        paintStats()
        return
      }
      var key = pickCard(keys, flatBoxes(), retry, asked, Math.random, lastKey)
      buildCard(key)
      paintStats()
    }

    function onKey(e) {
      if (e.ctrlKey || e.metaKey || e.altKey || !card || !document.body.contains(cardEl)) return
      var t = e.target
      if (t && (t.tagName === "BUTTON" || t.tagName === "SELECT" || t.tagName === "TEXTAREA")) return
      if (t && t.tagName === "INPUT" && t.type !== "text") return
      if (t && t.tagName === "INPUT") return // the box handles its own Enter
      if (e.key === "Enter") {
        e.preventDefault()
        if (card.answered) next()
        else if (card.submit) card.submit()
      } else if (!card.answered && card.buttons && /^[1-9]$/.test(e.key)) {
        var i = Number(e.key) - 1
        if (card.buttons[i]) {
          e.preventDefault()
          card.buttons[i].click()
        }
      }
    }
    document.addEventListener("keydown", onKey)

    reset.addEventListener("click", function () {
      state.boxes = {}
      counts = { right: 0, wrong: 0 }
      asked = 0
      retry = []
      persist()
      next()
    })

    if (!window.TWCharts) {
      cardEl.appendChild(h("p", { class: "tw-d-note", text: "The chart library did not load. Reload the page." }))
      return
    }
    paintSets()
    cardEl.appendChild(h("p", { class: "tw-d-note", text: "Loading..." }))
    var base = baseUrl()
    Promise.all(
      names.map(function (n) {
        return fetch(base + "assets/drills/" + n + ".json")
          .then(function (r) {
            if (!r.ok) throw new Error("status " + r.status)
            return r.json()
          })
          .then(function (d) { return { name: n, items: (d && d.items) || [] } })
          .catch(function () { return { name: n, items: null } })
      })
    ).then(function (res) {
      if (dead || !document.body.contains(root)) return
      var failed = []
      res.forEach(function (r) {
        if (!r.items) {
          failed.push(r.name)
          return
        }
        sets[r.name] = r.items
        r.items.forEach(function (it) { byKey[r.name + "/" + it.id] = { set: r.name, item: it } })
      })
      paintSets()
      next()
      if (failed.length) {
        root.appendChild(h("p", { class: "tw-d-note", text: "Could not load: " + failed.join(", ") + "." }))
      }
    })
  }

  function init() {
    cleanups.forEach(function (fn) { try { fn() } catch (e) { /* ignore */ } })
    cleanups = []
    document.querySelectorAll(".tw-drills[data-tool]").forEach(function (el) {
      if (el.dataset.built) return
      el.dataset.built = "1"
      if (el.getAttribute("data-tool") !== TOOL) {
        el.textContent = "This practice tool is not available."
        return
      }
      try {
        run(el)
      } catch (e) {
        el.textContent = "This practice tool could not start in this browser."
      }
    })
  }

  window.TWDrills = api
  var d$ = window.document$
  if (d$ && typeof d$.subscribe === "function") d$.subscribe(init)
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init)
  else init()
})()
