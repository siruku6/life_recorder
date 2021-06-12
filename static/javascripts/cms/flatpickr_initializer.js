window.addEventListener("load", function () {
  let pickr = flatpickr('.datepicker', {
    maxDate: 'today'
  });

  let $pickrIcons = document.getElementsByClassName('pickr-icon');
  Array.prototype.forEach.call($pickrIcons, function($pickrIcon, _index) {
    $pickrIcon.onclick = function () { pickr.open(); }
  });
});
