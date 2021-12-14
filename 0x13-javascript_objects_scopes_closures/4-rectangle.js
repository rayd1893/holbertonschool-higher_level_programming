#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (validate(w) !== undefined && validate(h) !== undefined) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const text = 'X';
    let i = 0;
    while (i < this.height) {
      console.log(text.repeat(this.width));
      i++;
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

function validate (n) {
  if (isNaN(parseInt(n)) || n <= 0) {
    return undefined;
  }
  return n;
}
module.exports = Rectangle;
