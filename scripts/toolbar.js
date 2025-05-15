fetch("/templates/toolbar.html") // Load toolbar from an external file
  .then(response => response.text())
  .then(data => document.getElementById("toolbar").innerHTML = data);

// get the footer
fetch("/templates/footer.html")
  .then(response => response.text())
  .then(data => document.getElementById("footer").innerHTML = data);
  


function toggleDropdown (element) {
  let dropdown = element.parentElement.querySelector(".dropdown-content");
  dropdown.style.display = (dropdown.style.display == "block") ? "none" : "block";
  console.log("click");
}

window.onclick = function(element) {
  if (!event.target.matches(".dropdown-btn")) {
    let dropdowns = document.getElementsByClassName(".dropdown-content");
    for (let i = 0; i < dropdowns.length; i++) {
      let thisDropdown = dropdowns[i];
      if (thisDropdown.style.display == "block") {
        thisDropdown.style.display = "none";
      }
    }
  }
}