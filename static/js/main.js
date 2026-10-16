(function () {
  var root = document.documentElement;
  var saved = localStorage.getItem("theme");
  if (saved) root.dataset.theme = saved;

  // 1. Переключатель темы
  var themeBtn = document.getElementById("theme-btn");
  if (themeBtn) themeBtn.onclick = function () {
    var next = root.dataset.theme === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    localStorage.setItem("theme", next);
  };

  // 2. Мобильное меню
  var menuBtn = document.getElementById("menu-btn"), nav = document.getElementById("nav");
  if (menuBtn) menuBtn.onclick = function () {
    menuBtn.setAttribute("aria-expanded", nav.classList.toggle("open"));
  };

  // 3. Мгновенный фильтр карточек по мере ввода
  var q = document.getElementById("q");
  if (q) q.addEventListener("input", function () {
    var v = q.value.trim().toLowerCase();
    document.querySelectorAll(".card").forEach(function (c) {
      c.classList.toggle("hidden", v !== "" && c.dataset.title.indexOf(v) < 0);
    });
  });

  // 4. Модальное окно подтверждения
  document.querySelectorAll("[data-open]").forEach(function (b) {
    b.onclick = function () { document.getElementById(b.dataset.open).showModal(); };
  });
  document.querySelectorAll("[data-close]").forEach(function (b) {
    b.onclick = function () { b.closest("dialog").close(); };
  });
})();
