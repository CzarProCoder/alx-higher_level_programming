#!/usr/bin/node
// JS script to display Movie title based on the movie ID passed
const request = require('request');
let url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
