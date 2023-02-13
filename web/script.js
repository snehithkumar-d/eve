function generateEvents() {
  var data = document.getElementById("data").value
  eel.generate_events(data)(function(data_list) {
    for (const [title, url, event_url] of data_list) {
      generate_events(title, url, event_url);
    }
  });
  // Clear the input field by setting the value to an empty string
  document.getElementById("data").value = ""
}

function generate_events(title, url, event_url) {
  var table = document.getElementById("event-table");
  var row = table.insertRow(-1);
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  cell1.innerHTML = title;
  cell2.innerHTML = url;
  cell3.innerHTML = event_url;
}

function copyData() {
  // Select the data in the first cell of the first row
  var data = document.querySelector("#event-table tr:first-child td:first-child").innerText;

  // Create a temporary element to hold the data
  var tempInput = document.createElement("input");
  tempInput.value = data;

  // Append the temporary element to the body
  document.body.appendChild(tempInput);

  // Select the data in the temporary element
  tempInput.select();

  // Copy the data
  document.execCommand("copy");

  // Remove the temporary element
  document.body.removeChild(tempInput);

  // Display a message to the user
  alert("Data copied to clipboard");
}

