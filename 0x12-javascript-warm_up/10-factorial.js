#!/usr/bin/node

const sysArg = process.argv.slice(2);
const n = parseInt(sysArg[0]);

const factorial = (num) => {
  // Base case: factorial of 0 or 1 is 1
  if (num === 0 || num === 1) {
    return 1;
  }
  // Handle case where num is NaN (not a number)
  if (isNaN(num)) {
    return 1;
  }
  // Recursive case: num * factorial of (num - 1)
  return num * factorial(num - 1);
};

const result = factorial(n);
console.log(result);
