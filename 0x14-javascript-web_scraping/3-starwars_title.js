#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, { json: true }, function (error, res, body) {
  if (error) {
    return console.log(error);
  }
  console.log(body.title);
});
