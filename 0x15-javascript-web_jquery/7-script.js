const url = 'https://swapi-api.alx-tools.com/api/people/7/?format=json';

$.get(url, function (data) {
  $('DIV#character').text(data.name);
});
