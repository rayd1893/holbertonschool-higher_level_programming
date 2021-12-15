#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c = 'X') {
    let i = 0;

    while (i < this.size) {
      console.log(c.repeat(this.size));
      i++;
    }
  }
}

module.exports = Square;
