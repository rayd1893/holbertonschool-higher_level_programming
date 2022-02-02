#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, { json: true }, function (error, res, body) {
  if (error) {
    return console.log(error);
  }
  for (const i of body.characters) {
    request(i, { json: true }, function (error, res, body) {
      if (error) {
        return console.log(error);
      }
      console.log(body.name);
    });
  }
});
