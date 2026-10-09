(function () {
  function normalize(value) {
    return value.toLowerCase().replace(/[\u0591-\u05c7]/g, "")
      .replace(/[ךםןףץ]/g, c => ({ך:"כ",ם:"מ",ן:"נ",ף:"פ",ץ:"צ"}[c]))
      .replace(/[^א-תa-z0-9]+/g, " ").trim();
  }
  function init(root) {
    if (!root || root.dataset.refReady) return;
    root.dataset.refReady = "true";
    const input = root.querySelector(".ref-search");
    const results = root.querySelector(".ref-results");
    const status = root.querySelector(".ref-status");
    const routes = [...root.querySelectorAll("[data-ref-route]")].map(node => ({
      id: node.id,
      title: node.dataset.refRoute,
      specific: node.tagName === "TR",
      primary: normalize(node.dataset.refRoute + " " + (node.dataset.refKeywords || "")),
      text: normalize(node.dataset.refRoute + " " + (node.dataset.refKeywords || "") + " " + node.textContent)
    }));
    function find(query) {
      const tokens = normalize(query).split(" ").filter(Boolean);
      return tokens.length ? routes.filter(route => tokens.every(token =>
        /^\d+$/.test(token) ? (" " + route.primary + " ").includes(" " + token + " ") : route.text.includes(token)
      )).sort((a,b) => {
        const score = r => (r.specific ? 100 : 0) + tokens.filter(t => normalize(r.title).includes(t)).length * 20;
        return score(b)-score(a);
      }) : [];
    }
    function render() {
      results.replaceChildren();
      const found = find(input.value);
      if (!input.value.trim()) { status.textContent = "חפשו נושא, סעיף עם שם החוק או פסק דין."; return found; }
      status.textContent = found.length ? found.length + " יעדים נמצאו. בחרו לפי שם החוק." : "לא נמצא יעד. נסו מילה אחת כמו ארכה, תושיה או הקטנת נזק; אפשר גם Ctrl+F.";
      for (const route of found) {
        const a = document.createElement("a");
        a.href = "#" + route.id;
        a.textContent = route.title;
        results.append(a);
      }
      return found;
    }
    function jump(id) {
      const target = root.querySelector("#" + id);
      if (!target) return;
      root.querySelectorAll(".ref-target").forEach(n => n.classList.remove("ref-target"));
      target.classList.add("ref-target");
      results.replaceChildren();
      status.textContent = "נפתח: " + (target.dataset.refRoute || target.querySelector("h2,h3")?.textContent || "מפתח");
      target.scrollIntoView({block:"start", behavior:"auto"});
      target.setAttribute("tabindex", "-1");
      target.focus({preventScroll:true});
    }
    input.addEventListener("input", render);
    root.querySelector(".ref-search-form").addEventListener("submit", event => {
      event.preventDefault();
      const found = render();
      if (found.length === 1) jump(found[0].id);
    });
    root.addEventListener("click", event => {
      const link = event.target.closest('a[href^="#exam-"]');
      if (link && root.contains(link)) { event.preventDefault(); jump(link.getAttribute("href").slice(1)); }
    });
    document.addEventListener("keydown", event => {
      if (!root.getClientRects().length || event.ctrlKey || event.metaKey || event.altKey) return;
      const typing = /INPUT|TEXTAREA|SELECT/.test(event.target.tagName) || event.target.isContentEditable;
      if (event.key === "/" && !typing) {
        event.preventDefault();
        input.scrollIntoView({block:"center"});
        input.focus();
      } else if (event.key === "Escape" && event.target === input) {
        input.value = "";
        render();
      }
    });
  }
  window.ExamReference = {init};
})();
