#!/usr/bin/node

const arg = process.argv.length;
let max;

if (arg <= 3) {
  console.log(0);
} else {
  process.argv.sort(function (a, b) {
    return b - a;
  });
  max = process.argv[2];

  for (const x of process.argv) {
    if (x < max && !Number.isNaN(parseInt(x))) {
      console.log(x);
      break;
    }
  }
}
