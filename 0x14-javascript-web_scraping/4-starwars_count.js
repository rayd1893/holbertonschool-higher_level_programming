#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, { json: true }, function (error, res, body) {
  if (error) {
    return console.log(error);
  }
  const results = body.results;
  let count = 0;
  for (const i of results) {
    for (const j of i.characters) {
      if (j.indexOf('18') > 0) {
        count += 1;
      }
    }
  }
  console.log(count);
});
