#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, { json: true }, function (error, res, body) {
  if (error) {
    return console.log(error);
  }
  const result = {};
  for (const i of body) {
    if (i.completed) {
      if (result[i.userId] === undefined) {
        result[i.userId] = 0;
      }
      result[i.userId] += 1;
    }
  }
  console.log(result);
});
