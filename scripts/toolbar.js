// inject toolbar styling
const toolbarLink = document.createElement('link');
toolbarLink.rel = "stylesheet";
toolbarLink.href = "/styles/toolbar.css";
document.head.appendChild(toolbarLink);

// inject variables styling
const globalLink = document.createElement('link');
globalLink.rel = "stylesheet";
globalLink.href = "/styles/globals.css";
document.head.appendChild(globalLink);

// inject footer styling
const footerLink = document.createElement('link');
footerLink.rel = "stylesheet";
footerLink.href = "/styles/footer.css";
document.head.appendChild(footerLink);

fetch("/templates/toolbar.html") // Load toolbar from an external file
  .then(response => response.text())
  .then(data => document.getElementById("toolbar").innerHTML = data);

// get the footer
fetch("/templates/footer.html")
  .then(response => response.text())
  .then(data => document.getElementById("footer").innerHTML = data);

  console.log(document.styleSheets);

  

function toggleDropdown (element) {
  let dropdown = element.parentElement.querySelector("dropdown-content");
  dropdown.style.display = (dropdown.style.display == "block") ? "none" : "block";
  console.log("click");
}

window.onclick = function(element) {
  if (!event.target.matches(".dropdown-btn")) {
    let dropdowns = document.getElementsByClassName("dropdown-content");
    for (let i = 0; i < dropdowns.length; i++) {
      let thisDropdown = dropdowns[i];
      if (thisDropdown.style.display == "block") {
        thisDropdown.style.display = "none";
      }
    }
  }
}