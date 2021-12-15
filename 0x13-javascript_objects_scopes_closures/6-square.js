#!/usr/bin/node

class Square extends require('./5-square') {
  charPrint (c = 'X') {
    let i = 0;

    while (i < this.height) {
      console.log(c.repeat(this.height));
      i++;
    }
  }
}

module.exports = Square;
