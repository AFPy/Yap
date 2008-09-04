function nextArticle(event) {
  alert('J');
}

function previousArticle(event) {
  alert('K');
}

// process keypresses
function navkey(event) {
  var checkbox = document.getElementById('navkeys');
  if (!checkbox || !checkbox.checked) return;

  if (!event) event=window.event;
  if (event.originalTarget &&
    event.originalTarget.nodeName.toLowerCase() == 'input' &&
    event.originalTarget.id != 'navkeys') return;

  if (!document.documentElement) return;
  if (!entries[0].anchor || !entries[0].anchor.offsetTop) return;

  key=event.keyCode;
  if (key == 'J'.charCodeAt(0)) nextArticle(event);
  if (key == 'K'.charCodeAt(0)) prevArticle(event);
}


