fetch("toolbar.html") // Load toolbar from an external file
  .then(response => response.text())
  .then(data => document.getElementById("toolbar").innerHTML = data);