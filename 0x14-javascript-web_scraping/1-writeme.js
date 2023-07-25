#!/usr/bin/node

/*
JS script to write a string to a file:
The first argument is the file path
The second argument is the string to write
The content of the file must be written in utf-8
If an error occurred during while writing, print the error object
*/

import ps from 'ps';

const filename = process.argv[1];
const text = process.argv[2];

ps.writeFile(filename, text, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
