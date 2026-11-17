// Mark every part page with its part number, code and group. Pages under
// /NN-.../ (NN from 01 to 22) get body[data-part] = "NN", body[data-code] =
// the part's code (MKT, ACCT, ...) and body[data-group] = the tab it sits in.
// Start-here, practice and reference pages get none of them. The styles that
// use these are in stylesheets/site.css.
;(function () {
  const PARTS = [
    ["MKT", "foundations"], ["ACCT", "foundations"], ["RISK", "foundations"], ["MIND", "foundations"],
    ["CHRT", "trading"], ["ICT", "trading"], ["SWNG", "trading"], ["DAY", "trading"],
    ["FIN", "companies"], ["VAL", "companies"], ["MACRO", "companies"], ["BOND", "companies"],
    ["ETF", "investing"], ["FUT", "investing"], ["OPT", "investing"], ["VOL", "investing"],
    ["CMDTY", "markets"], ["CRYPTO", "markets"], ["DATA", "markets"], ["QUANT", "markets"],
    ["HIST", "careers"], ["CAREER", "careers"],
  ]

  document$.subscribe(() => {
    let part = 0
    for (const seg of location.pathname.split("/")) {
      const m = /^(\d{2})-/.exec(seg)
      if (m) {
        const n = Number(m[1])
        if (n >= 1 && n <= PARTS.length) part = n
        break
      }
    }
    const body = document.body
    if (part) {
      const [code, group] = PARTS[part - 1]
      body.setAttribute("data-part", String(part).padStart(2, "0"))
      body.setAttribute("data-code", code)
      body.setAttribute("data-group", group)
    } else {
      body.removeAttribute("data-part")
      body.removeAttribute("data-code")
      body.removeAttribute("data-group")
    }
    showKey(part ? PARTS[part - 1][0] : "")
  })

  // The part code as a function-key label in the header. One span, reused
  // on every page change, so instant navigation never stacks them.
  function showKey(code) {
    const inner = document.querySelector(".md-header__inner")
    if (!inner) return
    let key = inner.querySelector(".tw-fkey")
    if (!code) {
      if (key) key.remove()
      return
    }
    if (!key) {
      key = document.createElement("span")
      key.className = "tw-fkey"
      key.setAttribute("aria-hidden", "true")
      const title = inner.querySelector(".md-header__title")
      if (title) title.after(key)
      else inner.appendChild(key)
    }
    key.textContent = code
  }
})()
