#!/usr/bin/node

// Script todisplay status code of a GET Request

const request = require('request');
const url = process.argv[2];

request(url, function (error, response){
  if (err) {
    console.log(err);
  } else {
  console.log('Code: ' + response.statusCode);
    }
  });
