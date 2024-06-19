#!/usr/bin/node

const sysArg = process.argv.slice(2);
const arg1 = sysArg[0];
const char = sysArg[1] || 'X';

const areaOfSquare = (size, char) => {
  for (let i = 0; i < size; i++) {
    console.log(char.repeat(size));
  }
};

const Square = (arg1) => {
  if (isNaN(arg1)) {
    console.log('Missing size');
  } else {
    const value = parseInt(arg1);
    areaOfSquare(value, char);
  }
};

Square(arg1);
