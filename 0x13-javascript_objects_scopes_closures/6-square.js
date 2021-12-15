#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = undefined) {
    let text = 'X';
    let i = 0;

    if (c !== undefined) {
      text = c;
    }
    while (i < this.height) {
      console.log(text.repeat(this.width));
      i++;
    }
  }
}

module.exports = Square;
