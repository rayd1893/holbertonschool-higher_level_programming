#!/usr/bin/node

const first = parseInt(process.argv[2]);
let result;

if (Number.isNaN(first)) {
  result = 'Not a number';
} else {
  result = 'My number: ' + first;
}

console.log(result);
