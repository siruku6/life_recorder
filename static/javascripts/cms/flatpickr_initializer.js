function getStringFromDate(date, format) {
  var year_str = date.getFullYear();
  var month_str = 1 + date.getMonth(); // 月だけ+1
  var day_str = date.getDate();
  var hour_str = date.getHours();
  var minute_str = date.getMinutes();
  var second_str = date.getSeconds();

  month_str = ('0' + month_str).slice(-2);
  day_str = ('0' + day_str).slice(-2);
  hour_str = ('0' + hour_str).slice(-2);
  minute_str = ('0' + minute_str).slice(-2);
  second_str = ('0' + second_str).slice(-2);

  // format_str = 'YYYY-MM-DD hh:mm:ss';
  format_str = format;
  format_str = format_str.replace(/YYYY/g, year_str);
  format_str = format_str.replace(/MM/g, month_str);
  format_str = format_str.replace(/DD/g, day_str);
  format_str = format_str.replace(/hh/g, hour_str);
  format_str = format_str.replace(/mm/g, minute_str);
  format_str = format_str.replace(/ss/g, second_str);
  return format_str;
};


window.addEventListener("load", function () {
  // INFO: DatePickr
  let datepickr = flatpickr('.datepickr', {
    maxDate: 'today'
  });

  let $datepickrIcons = document.getElementsByClassName('datepickr-icon');
  Array.prototype.forEach.call($datepickrIcons, function($datepickrIcon, _index) {
    $datepickrIcon.onclick = function () { datepickr.toggle(); }
  });

  // https://flatpickr.js.org/examples/
  // Custom parsing and formating
  // INFO: TimePickr
  let timepickr = flatpickr('.timepickr', {
    enableTime: true,
    noCalendar: true,
    time_24hr: true,
    dateFormat: 'H:i',
    defaultMinute: 0,
    // defaultDate: "13:45",
    minuteIncrement: 15,
    parseDate: (datestr, _format) => {
      return new Date(datestr);
    },
    formatDate: (date, _format, _locale) => {
      // locale can also be used
      return getStringFromDate(date, 'hh:mm');
    }
  });

  let $timepickrIcons = document.getElementsByClassName('timepickr-icon');
  Array.prototype.forEach.call($timepickrIcons, function($timepickrIcon, index) {
    $timepickrIcon.onclick = function () { timepickr[index].toggle(); }
  });
});
