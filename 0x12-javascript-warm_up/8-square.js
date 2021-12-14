#!/usr/bin/node

const number = parseInt(process.argv[2]);
const text = 'X';
let i = 0;

if (Number.isNaN(number)) {
  console.log('Missing size');
} else {
  while (i < number) {
    console.log(text.repeat(number));
    i++;
  }
}
