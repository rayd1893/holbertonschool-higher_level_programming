#!/usr/bin/node

const number = parseInt(process.argv[2]);
const text = 'C is fun';
let i = 0;

if (Number.isNaN(number)) {
  console.log('Missing number of occurrences');
}

while (i < number) {
  console.log(text);
  i++;
}
