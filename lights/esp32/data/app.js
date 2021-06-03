
  function call(request) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/" + request, true);
    xhr.send();
  }

  function toggleCheckbox(element) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/update?color=" + element.id + "&value=" + (element.checked ? 1 : 0), true);
    xhr.send();
  }

  if (!!window.EventSource) {
    var source = new EventSource('/events');

    source.addEventListener('open', function(e) {
      console.log("Events Connected");
    }, false);

    source.addEventListener('error', function(e) {
      if (e.target.readyState != EventSource.OPEN) {
        console.log("Events Disconnected");
      }
    }, false);

    source.addEventListener('message', function(e) {
      console.log("message", e.data);
    }, false);

    source.addEventListener('pin', function(e) {
      values = e.data.split(' ');
      console.log(values);
      document.getElementById('r').checked = parseInt(values[0]);
      document.getElementById('y').checked = parseInt(values[1]);
      document.getElementById('g').checked = parseInt(values[2]);
    }, false);
  }