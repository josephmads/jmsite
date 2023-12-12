// Toggles between Light and Dark Mode
const btn = document.getElementById("toggle-mode");
const theme = document.querySelector("#theme-link")

function darkMode() {
  if (theme.getAttribute("href") == "{% static 'base/css/light-theme.css' %}") {
    theme.href = "{% static 'base/css/dark-theme.css' %}";
  } else {
    theme.href = "{% static 'base/css/light-theme.css' %}";
  }
  if (btn.innerHTML === "Dark Mode") {
      btn.innerHTML = "Light Mode";
  } else {
      btn.innerHTML = "Dark Mode";
  }
}

btn.addEventListener("click", darkMode);
