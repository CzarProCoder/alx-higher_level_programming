#!/usr/bin/node

/*
   JS script to read and print contents of a file
 */

const fs = require('fs');
const filepath = process.argv[2];

fs.readFile(filepath, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
