#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, { json: true }, function (error, res, body) {
  if (error) {
    return console.log(error);
  }
  const results = body.results;
  let count = 0;
  for (const i in results) {
    for (const j in results[i].characters) {
      const characters = results[i].characters;
      if (characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        count += 1;
      }
    }
  }
  console.log(count);
});
