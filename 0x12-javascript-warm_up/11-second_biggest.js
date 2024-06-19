#!/usr/bin/node
const arg = process.argv.slice(2);

if (!arg) {
  console.log(0);
} else if (arg.length < 2) {
  console.log(0);
} else {
  console.log(arg.sort()[arg.length - 2]);
}
