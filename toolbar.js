fetch("https://bitflip.club/templates/toolbar.html") // Load toolbar from an external file
  .then(response => response.text())
  .then(data => document.getElementById("toolbar").innerHTML = data);

// get the footer
fetch("https://bitflip.club/templates/footer.html")
  .then(response => response.text())
  .then(data => document.getElementById("footer").innerHTML = data);
  