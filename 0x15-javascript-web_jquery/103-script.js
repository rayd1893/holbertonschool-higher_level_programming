$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    print_hello();
  });

  $(document).keypress(function (e) {
    if (e.which == 13) {
      print_hello();
    }
  });
});

function print_hello () {
  const lang = $('INPUT#language_code').val();
  const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
  $.get(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
}
