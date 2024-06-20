#!/usr/bin/node
// class Rectangle

class Rectangle {
  constructor (w, h) {
    if (this._isValidDimension(w) && this._isValidDimension(h)) {
      this.width = w;
      this.height = h;
    } else {
      return null;
    }
  }

  _isValidDimension (value) {
    return Number.isInteger(value) && value > 0;
  }

  // an instance called print
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
