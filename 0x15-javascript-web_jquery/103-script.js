/* global $ */
$(document).ready(function () {
  function fetchGreeting () {
    const langCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchGreeting);

  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      fetchGreeting();
    }
  });
});
