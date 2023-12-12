// Toggles between Light and Dark Mode
const btn = document.getElementById("toggle-mode");
const themeLink = document.getElementById("theme-link");

// Sets theme to Dark Mode and saves user selection to localStorage
btn.addEventListener("click", () => {
  if (themeLink.getAttribute("href") === "/static/base/css/light-theme.css") {
    themeLink.href = "/static/base/css/dark-theme.css";
    localStorage.setItem('theme', 'dark');
  } else {
    themeLink.href = "/static/base/css/light-theme.css";
    localStorage.setItem('theme', 'light');
  }
});

// Loads user selection from localStorage
window.onload = () => {
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
      const themeLink = document.getElementById('theme-link');
      themeLink.href = `/static/base/css/${savedTheme}-theme.css`;
  }
};
