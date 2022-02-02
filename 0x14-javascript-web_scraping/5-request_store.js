#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const file = process.argv[3];
const url = process.argv[2];
request(url, function (error, res, body) {
  if (error) {
    return console.log(error);
  }
  const content = body;
  fs.writeFile(file, content, 'utf8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
