#!/usr/bin/node
const arg = process.argv.slice(2);

if (arg.length < 2) {
  console.log(0);
} else {
  console.log(arg.sort()[arg.length - 2]);
}
