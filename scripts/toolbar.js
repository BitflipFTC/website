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


// let dropdownContent = document.getElementsByClassName("dropdown-content")[0];
// while(dropdownContent == null) {
//   dropdownContent = document.getElementsByClassName("dropdown-content")[0];
// }


const observer = new MutationObserver((mutationsList, observer) => {
    let dropdownContent = document.getElementsByClassName("dropdown-content")[0];
    if (dropdownContent) {
        console.log("Dropdown found!", dropdownContent);

        dropdownContent.style.opacity = window.getComputedStyle(dropdownContent).opacity;

        observer.disconnect(); // Stop observing once found
    }
});

observer.observe(document.body, { childList: true, subtree: true });




function toggleDropdown (element) {
  let dropdown = element.parentElement.querySelector(".dropdown-content");
  // dropdown.style.display = (dropdown.style.display == "block") ? "none" : "block";
  console.log("Opacity:", window.getComputedStyle(dropdown).opacity); 
  dropdown.style.opacity = (dropdown.style.opacity == "0") ? "1" : "0";
  dropdown.style.pointerEvents = (dropdown.style.opacity == "1") ? "all" : "none";
  console.log("toggle dropdown");
  console.log("new pointer events: " + dropdown.style.pointerEvents);
}

window.addEventListener("click", function(event) {
  if (!event.target.matches(".dropdown-btn")) {
    let dropdowns = document.getElementsByClassName("dropdown-content");
    for (let i = 0; i < dropdowns.length; i++) {
      let thisDropdown = dropdowns[i];
      console.log("test1");
      if (thisDropdown.style.opacity == "1") {
        toggleDropdown(thisDropdown);
      }
    }
  }
});