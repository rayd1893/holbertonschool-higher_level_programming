#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, res) {
  console.log('code: ' + res.statusCode);
  if (error) {
    console.log(error);
  }
});
