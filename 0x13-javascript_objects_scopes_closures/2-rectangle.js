#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (validate(w) !== undefined && validate(h) !== undefined) {
      this.width = w;
      this.height = h;
    }
  }
}

function validate (n) {
  if (isNaN(parseInt(n)) || n <= 0) {
    return undefined;
  }
  return n;
}
module.exports = Rectangle;
