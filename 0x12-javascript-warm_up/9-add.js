#!/usr/bin/node

const sysArg = process.argv.slice(2);
const arg1 = sysArg[0];
const arg2 = sysArg[1];

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(arg1, arg2);
