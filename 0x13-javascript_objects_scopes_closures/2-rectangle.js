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
}

module.exports = Rectangle;

// if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
//   this.width = w;
//   this.height = h;
// } else {
//   return;
// }
