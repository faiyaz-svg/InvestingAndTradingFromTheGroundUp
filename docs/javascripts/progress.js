// Make the checkboxes on the progress page clickable and remember them in
// this browser (localStorage). Each device keeps its own list. On the home
// page, the DONE column of the watchlist fills in from the same list.
const TW_PROGRESS_KEY = "itftgu-progress-v1"

function twLoadProgress() {
  try {
    return JSON.parse(localStorage.getItem(TW_PROGRESS_KEY)) || {}
  } catch (e) {
    return {}
  }
}

function twSaveProgress(state) {
  try {
    localStorage.setItem(TW_PROGRESS_KEY, JSON.stringify(state))
  } catch (e) {
    // Storage blocked (private mode): ticks last until the page closes.
  }
}

// The site root, worked out once from this script's own URL (javascripts/x.js).
// The __config base is relative to the first page loaded, so it goes stale
// after instant navigation; the script URL does not.
var TW_SITE_ROOT = (function () {
  try {
    var s = typeof document !== "undefined" && document.currentScript && document.currentScript.src
    if (s) return new URL("../", s).href
  } catch (e) { /* fall through */ }
  return null
})()

function twBasePath() {
  if (TW_SITE_ROOT) return new URL(TW_SITE_ROOT).pathname
  const key = "/InvestingAndTradingFromTheGroundUp/"
  const i = location.pathname.indexOf(key)
  return i >= 0 ? location.pathname.slice(0, i + key.length) : "/"
}

// A lesson's key: its URL path without the base, such as "01-how-markets-work/01-what-a-stock-is/".
function twLessonKey(pathname) {
  const base = twBasePath()
  let key = pathname.startsWith(base) ? pathname.slice(base.length) : pathname.replace(/^\//, "")
  if (key && !key.endsWith("/")) key += "/"
  return key
}

document$.subscribe(() => {
  const state = twLoadProgress()

  // The home page watchlist.
  document.querySelectorAll("tr.tw-part").forEach((row) => {
    const total = Number(row.getAttribute("data-total")) || 0
    const lessons = (row.getAttribute("data-lessons") || "").split(" ").filter(Boolean)
    const done = lessons.filter((key) => state[key] === true).length
    const pct = total ? Math.round((100 * done) / total) : 0
    const fill = row.querySelector(".tw-fill")
    const label = row.querySelector(".tw-pct")
    if (fill) fill.style.width = pct + "%"
    if (label) label.textContent = pct + "%"
    row.classList.toggle("tw-started", done > 0)
    row.classList.toggle("tw-finished", total > 0 && done === total)
  })

  const article = document.querySelector("article.md-content__inner")
  if (!article || !location.pathname.replace(/\/$/, "").endsWith("/progress")) return

  const items = article.querySelectorAll("li.task-list-item")
  let total = 0

  items.forEach((li) => {
    const box = li.querySelector("input[type=checkbox]")
    const link = li.querySelector("a")
    if (!box || !link) return
    const key = twLessonKey(new URL(link.href, location.href).pathname)
    total += 1
    box.disabled = false
    box.classList.add("tw-progress-box")
    if (key in state) box.checked = state[key]
    box.addEventListener("change", () => {
      state[key] = box.checked
      twSaveProgress(state)
      updateCount()
    })
  })

  const count = document.createElement("p")
  count.className = "tw-progress-count"
  const h1 = article.querySelector("h1")
  if (h1) h1.after(count)

  function updateCount() {
    const checked = article.querySelectorAll("input.tw-progress-box:checked").length
    count.textContent = `Finished in this browser: ${checked} of ${total} written lessons.`
  }
  updateCount()
})
