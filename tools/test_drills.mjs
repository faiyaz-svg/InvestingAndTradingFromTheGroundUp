// Run with: node --test tools/test_drills.mjs
import { test } from "node:test"
import assert from "node:assert/strict"
import { createRequire } from "node:module"

const require = createRequire(import.meta.url)
const drills = require("../docs/javascripts/drills.js")
const charts = require("../docs/javascripts/charts.js")

const { parseNumber, gradeNumber, grade, boxOf, finish, nextCard, scheduleRetry, dueRetry, pickCard, boxCounts, weightOf } = drills
const { ind, parseSpec, parseTime } = charts

const near = (a, b, eps = 1e-9) => assert.ok(Math.abs(a - b) < eps, `${a} is not ${b}`)

// ---------- parseNumber ----------

test("parseNumber accepts common forms", () => {
  assert.equal(parseNumber("1,250.50"), 1250.5)
  assert.equal(parseNumber("$48.20"), 48.2)
  assert.equal(parseNumber("US$48.20"), 48.2)
  assert.equal(parseNumber("us$ 48.20"), 48.2)
  assert.equal(parseNumber("CA$48.20"), 48.2)
  assert.equal(parseNumber(" 48.2 "), 48.2)
  assert.equal(parseNumber("-3.5"), -3.5)
  assert.equal(parseNumber("-$3.5"), -3.5)
  assert.equal(parseNumber("−3.5"), -3.5)
  assert.equal(parseNumber(".5"), 0.5)
  assert.equal(parseNumber("7"), 7)
  assert.equal(parseNumber("7."), 7)
  assert.equal(parseNumber(12.5), 12.5)
})

test("parseNumber rejects junk", () => {
  for (const bad of ["", "   ", "abc", "1.2.3", "--3", "4 5x", "$", null, undefined, NaN, Infinity]) {
    assert.equal(parseNumber(bad), null, String(bad))
  }
})

// ---------- grade ----------

test("grade level and number use an inclusive tolerance", () => {
  const item = { type: "level", answer: 100.29, tolerance: 0.6 }
  assert.equal(grade(item, 100.29), true)
  assert.equal(grade(item, 100.89), true) // exactly on the edge
  assert.equal(grade(item, 99.69), true)
  assert.equal(grade(item, 100.9), false)
  assert.equal(grade(item, 99.68), false)
  const num = { type: "number", answer: 48.2, tolerance: 0.1 }
  assert.equal(grade(num, 48.3), true)
  assert.equal(grade(num, 48.31), false)
  assert.equal(grade(num, 48.1), true)
  assert.equal(grade(num, 48.09), false)
})

test("grade handles bad input", () => {
  const item = { type: "number", answer: 5, tolerance: 1 }
  assert.equal(grade(item, null), false)
  assert.equal(grade(item, NaN), false)
  assert.equal(grade(item, undefined), false)
  assert.equal(gradeNumber("5", 5, 1), false)
})

test("grade choice", () => {
  const item = { type: "choice", choices: ["a", "b", "c"], answer_choice: 0 }
  assert.equal(grade(item, 0), true)
  assert.equal(grade(item, 1), false)
  assert.equal(grade(item, "0"), false)
  assert.equal(grade({ type: "choice", answer_choice: 2 }, 2), true)
})

// ---------- Leitner ----------

test("boxOf and finish", () => {
  const boxes = {}
  assert.equal(boxOf(boxes, "a"), null)
  finish(boxes, "a", true)
  assert.equal(boxOf(boxes, "a"), 1)
  finish(boxes, "a", true)
  finish(boxes, "a", true)
  finish(boxes, "a", true)
  assert.equal(boxOf(boxes, "a"), 4)
  finish(boxes, "a", true)
  assert.equal(boxOf(boxes, "a"), 4) // capped
  finish(boxes, "a", false)
  assert.equal(boxOf(boxes, "a"), 0)
  finish(boxes, "b", false) // a new card that is missed
  assert.equal(boxOf(boxes, "b"), 0)
  assert.equal(boxOf({ x: 9 }, "x"), null)
  assert.equal(boxOf({ x: -1 }, "x"), null)
  assert.equal(boxOf({ x: "2" }, "x"), null)
})

test("weights: lower boxes come up more", () => {
  assert.ok(weightOf(0) > weightOf(1))
  assert.ok(weightOf(1) > weightOf(2))
  assert.ok(weightOf(3) > weightOf(4))
  assert.ok(weightOf(null) > weightOf(1))
})

test("nextCard is weighted, avoids the last card, handles one card", () => {
  const ids = ["a", "b", "c"]
  const boxes = { a: 0, b: 4, c: 4 }
  // roll just under the first weight picks "a"; the last roll picks the last id
  assert.equal(nextCard(ids, boxes, () => 0, undefined), "a")
  assert.equal(nextCard(ids, boxes, () => 0.9999, undefined), "c")
  // with a avoided, the pool is b, c
  assert.equal(nextCard(ids, boxes, () => 0, "a"), "b")
  // a single card is returned even if avoided
  assert.equal(nextCard(["z"], {}, () => 0.5, "z"), "z")
  assert.equal(nextCard([], {}, () => 0.5), undefined)
  // frequency: box 0 beats box 4 by about 16 to 1
  let a = 0
  let n = 0
  let seed = 12345
  const rand = () => ((seed = (seed * 1664525 + 1013904223) % 4294967296) / 4294967296)
  for (let i = 0; i < 4000; i++) {
    const pick = nextCard(["x", "y"], { x: 0, y: 4 }, rand)
    if (pick === "x") a++
    n++
  }
  assert.ok(a / n > 0.9, `x share ${a / n}`)
})

test("missed cards come back after a few cards", () => {
  const ids = ["a", "b", "c", "d", "e", "f"]
  const retry = []
  scheduleRetry(retry, "a", 5, ids)
  assert.deepEqual(retry, [{ id: "a", due: 8 }])
  assert.equal(dueRetry(retry, 7, ids), undefined)
  assert.equal(retry.length, 1)
  assert.equal(dueRetry(retry, 8, ids), "a")
  assert.equal(retry.length, 0)
  // a small pool brings it back on the next card
  const small = []
  scheduleRetry(small, "a", 2, ["a", "b"])
  assert.equal(small[0].due, 3)
  // a retry for a card no longer in the pool is dropped
  const gone = [{ id: "q", due: 0 }]
  assert.equal(dueRetry(gone, 5, ids), undefined)
  assert.equal(gone.length, 0)
})

test("pickCard prefers a due retry but not the card just shown", () => {
  const ids = ["a", "b", "c"]
  const retry = [{ id: "b", due: 1 }]
  assert.equal(pickCard(ids, {}, retry, 1, () => 0, "a"), "b")
  const again = [{ id: "b", due: 1 }]
  const p = pickCard(ids, {}, again, 1, () => 0, "b")
  assert.notEqual(p, "b")
  assert.equal(again.length, 1) // kept for later
})

test("boxCounts", () => {
  const c = boxCounts(["a", "b", "c", "d"], { a: 0, b: 0, c: 3 })
  assert.deepEqual(c, { fresh: 1, 0: 2, 1: 0, 2: 0, 3: 1, 4: 0 })
})

// ---------- charts.js: indicators, checked against hand calculations ----------

test("sma", () => {
  const out = ind.sma([1, 2, 3, 4, 5], 3)
  assert.deepEqual(out, [null, null, 2, 3, 4])
  assert.deepEqual(ind.sma([1, 2], 3), [null, null])
})

test("ema is seeded by the sma", () => {
  // n=3, k=0.5. Seed (2+4+6)/3 = 4. Then 5*.5+4*.5 = 4.5, then 9*.5+4.5*.5 = 6.75.
  const out = ind.ema([2, 4, 6, 5, 9], 3)
  assert.equal(out[0], null)
  assert.equal(out[1], null)
  near(out[2], 4)
  near(out[3], 4.5)
  near(out[4], 6.75)
  assert.deepEqual(ind.ema([1, 2], 3), [null, null])
})

test("rsi with Wilder smoothing", () => {
  // closes 10 11 10 12 13 12, n=3
  // gains (from bar 1) 1 0 2 1 0, losses 0 1 0 0 1
  // seed at bar 3: avg gain 1, avg loss 1/3 -> RS 3 -> RSI 75
  // bar 4: gain (1*2+1)/3 = 1, loss (1/3*2+0)/3 = 2/9 -> RS 4.5 -> 100 - 100/5.5
  // bar 5: gain 2/3, loss (2/9*2+1)/3 = 13/27 -> RS 18/13 -> 100*18/31
  const out = ind.rsi([10, 11, 10, 12, 13, 12], 3)
  assert.deepEqual(out.slice(0, 3), [null, null, null])
  near(out[3], 75)
  near(out[4], 100 - 100 / 5.5)
  near(out[5], (100 * 18) / 31)
})

test("rsi edge cases", () => {
  const up = ind.rsi([1, 2, 3, 4, 5], 3)
  assert.equal(up[3], 100)
  const flat = ind.rsi([5, 5, 5, 5, 5], 3)
  assert.equal(flat[3], 50)
})

test("true range and atr", () => {
  const bars = [
    { high: 10, low: 8, close: 9 },
    { high: 11, low: 9, close: 10 },
    { high: 12, low: 9, close: 11 },
    { high: 12, low: 10, close: 11 },
  ]
  // TR: 2, max(2,|11-9|,|9-9|)=2, max(3,|12-10|,|9-10|)=3, max(2,1,1)=2
  assert.deepEqual(ind.trueRange(bars), [2, 2, 3, 2])
  const a = ind.atr(bars, 3)
  assert.deepEqual(a.slice(0, 2), [null, null])
  near(a[2], 7 / 3)
  near(a[3], 20 / 9) // (7/3*2 + 2) / 3
})

test("bollinger uses the population standard deviation", () => {
  const b = ind.bollinger([1, 2, 3, 4], 3, 2)
  const sd = Math.sqrt(2 / 3) // values 1,2,3 around mean 2: (1+0+1)/3
  assert.equal(b.mid[1], null)
  near(b.mid[2], 2)
  near(b.upper[2], 2 + 2 * sd)
  near(b.lower[2], 2 - 2 * sd)
  near(b.mid[3], 3)
  near(b.upper[3], 3 + 2 * sd)
})

test("vwap on three bars", () => {
  const bars = [
    { time: "2026-01-05", high: 12, low: 8, close: 10, volume: 100 }, // tp 10
    { time: "2026-01-06", high: 13, low: 9, close: 11, volume: 200 }, // tp 11
    { time: "2026-01-07", high: 16, low: 10, close: 13, volume: 100 }, // tp 13
  ]
  const v = ind.vwap(bars, 0, false)
  near(v[0], 10)
  near(v[1], 3200 / 300)
  near(v[2], 4500 / 400)
  const anchored = ind.vwap(bars, 1, false)
  assert.equal(anchored[0], null)
  near(anchored[1], 11)
  near(anchored[2], 3500 / 300)
})

test("intraday vwap restarts each session", () => {
  const day1 = Date.parse("2026-03-02T15:55:00Z") / 1000
  const day2 = Date.parse("2026-03-03T09:30:00Z") / 1000
  const bars = [
    { time: day1, high: 10, low: 10, close: 10, volume: 100 },
    { time: day2, high: 20, low: 20, close: 20, volume: 100 },
  ]
  const v = ind.vwap(bars, 0, true)
  near(v[0], 10)
  near(v[1], 20) // not 15
})

test("macd lines line up", () => {
  const closes = Array.from({ length: 40 }, (_, i) => 100 + i + (i % 3))
  const m = ind.macd(closes, 3, 6, 2)
  assert.equal(m.line[4], null)
  assert.notEqual(m.line[5], null)
  assert.equal(m.signal[5], null)
  assert.notEqual(m.signal[6], null)
  near(m.hist[10], m.line[10] - m.signal[10])
})

test("stochastic on a short series", () => {
  const bars = [
    { high: 10, low: 5, close: 6 },
    { high: 11, low: 6, close: 10 },
    { high: 12, low: 7, close: 12 },
  ]
  // n=2, smooth 1, d 1: bar1 raw = 100*(10-5)/(11-5), bar2 raw = 100*(12-6)/(12-6)
  const s = ind.stoch(bars, 2, 1, 1)
  assert.equal(s.k[0], null)
  near(s.k[1], (100 * 5) / 6)
  near(s.k[2], 100)
})

// ---------- charts.js: the fence ----------

test("parseSpec reads every key", () => {
  const spec = parseSpec(`
# a comment
data: samples/daily-trend-pullback.json
title: Stock A, daily
type: line
height: 420
show: volume, sma 20, ema 50, bb 20 2, rsi 14, macd 12 26 9
level: 104.20 | Support
level: 110
zone: 101.5-103.0 | Fair value gap
zone: 101.50-103.00 | 2026-03-02 to 2026-03-20 | FVG
marker: 2026-03-14 | below | Entry
marker: 2026-03-20 | above | Exit
line: 2026-02-02 96.4 to 2026-03-10 103.8 | Trendline
range: 2026-02-01 to 2026-04-30
caption: The pullback held.
`)
  assert.equal(spec.data, "samples/daily-trend-pullback.json")
  assert.equal(spec.title, "Stock A, daily")
  assert.equal(spec.type, "line")
  assert.equal(spec.height, 420)
  assert.deepEqual(spec.show, [["volume"], ["sma", "20"], ["ema", "50"], ["bb", "20", "2"], ["rsi", "14"], ["macd", "12", "26", "9"]])
  assert.deepEqual(spec.levels, [{ price: 104.2, label: "Support" }, { price: 110, label: "" }])
  assert.deepEqual(spec.zones[0], { low: 101.5, high: 103, from: null, to: null, label: "Fair value gap" })
  assert.deepEqual(spec.zones[1], { low: 101.5, high: 103, from: "2026-03-02", to: "2026-03-20", label: "FVG" })
  assert.deepEqual(spec.markers, [
    { time: "2026-03-14", position: "below", text: "Entry" },
    { time: "2026-03-20", position: "above", text: "Exit" },
  ])
  assert.deepEqual(spec.lines, [{ t1: "2026-02-02", p1: 96.4, t2: "2026-03-10", p2: 103.8, label: "Trendline" }])
  assert.deepEqual(spec.range, { from: "2026-02-01", to: "2026-04-30" })
  assert.equal(spec.caption, "The pullback held.")
})

test("parseSpec clamps height and handles intraday times", () => {
  assert.equal(parseSpec("height: 50").height, 200)
  assert.equal(parseSpec("height: 5000").height, 700)
  assert.equal(parseSpec("data: x.json").height, 360)
  const s = parseSpec("line: 2026-03-02 10:00 200.5 to 2026-03-02 12:00 203 | Trend\nrange: 2026-03-02 09:30 to 2026-03-02 16:00")
  assert.deepEqual(s.lines[0], { t1: "2026-03-02 10:00", p1: 200.5, t2: "2026-03-02 12:00", p2: 203, label: "Trend" })
  assert.deepEqual(s.range, { from: "2026-03-02 09:30", to: "2026-03-02 16:00" })
})

test("the reveal lines can be appended to a fence", () => {
  const spec = parseSpec("data: a.json\nshow: volume\n\nlevel: 100.29 | Pullback low")
  assert.deepEqual(spec.levels, [{ price: 100.29, label: "Pullback low" }])
})

test("parseTime", () => {
  assert.equal(parseTime("2026-03-02", false), "2026-03-02")
  assert.equal(parseTime("2026-03-02 09:30", true), Date.UTC(2026, 2, 2, 9, 30) / 1000)
  const first = Date.UTC(2026, 2, 2, 9, 30) / 1000
  assert.equal(parseTime("10:00", true, first), Date.UTC(2026, 2, 2, 10, 0) / 1000)
})
