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

  //   an insance that exchange the width and height of the rectangle.
  rotate () {
    [this.height, this.width] = [this.width, this.height];
    // const tempHeight = this.height;
    // this.height = this.width;
    // this.width = tempHeight;
  }

  //   an insance that multiplies the width and height of the rectangle.
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
