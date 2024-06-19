#!/usr/bin/node
const arg = process.argv.slice(2).map(Number);

if (arg.length === 0 || arg.length === 1) {
  console.log(0);
} else {
  const secondlargest = arg.sort((a, b) => b - a)[1];
  console.log(secondlargest);
}
