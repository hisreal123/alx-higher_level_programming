#!/usr/bin/node

const sysArg = process.argv.slice(2);
const n = parseInt(sysArg[0]);

const factorial = (num) => {
  if (Number.isNaN(num)) {
    return 1;
  }
  if (isNaN(num)) {
    return 1;
  }
  return num * factorial(num - 1);
};

const result = factorial(n);
console.log(result);
