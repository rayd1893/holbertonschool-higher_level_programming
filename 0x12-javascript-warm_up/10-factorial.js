#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (Number.isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}

function factorial (n) {
  if (n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
