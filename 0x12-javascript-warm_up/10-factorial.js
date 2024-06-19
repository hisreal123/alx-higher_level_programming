#!/usr/bin/node

const n = Number(process.argv.slice(2));

const factorial = (num) => {
  if (Number.isNaN(num) || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
};

console.log(factorial(n));
