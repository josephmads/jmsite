function copyDate() {
  let footer = document.getElementById("copyright");
  let copyrightText = "Copyright © Joseph Madsen " + new Date().getFullYear();
  footer.innerText = copyrightText;
}

copyDate();
