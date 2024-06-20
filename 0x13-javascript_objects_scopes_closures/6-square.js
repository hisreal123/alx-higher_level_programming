#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  size;
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  //    prints the rectangle using the c
  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
