chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
  var currentUrl = tabs[0].url;
  var urlDisplay = document.getElementById('url');
  urlDisplay.innerHTML = 'Current URL: ' + currentUrl;
  
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://localhost:5000/data');
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.onload = function() {
    if (xhr.status === 200) {
      var data = JSON.parse(xhr.responseText);
      var output = document.getElementById('output');
      output.innerHTML = 'Array retrieved: ' + data.toString(); 
    }
  };
  xhr.send(JSON.stringify({url: currentUrl}));
  
});