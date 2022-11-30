#!/usr/bin/node
const squareOne = require('./5-square');

class Square extends squareOne {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i = 0;
      while (i < this.height) {
        console.log(c.repeat(this.width));
        i += 1;
      }
    }
  }
}

module.exports = Square;
