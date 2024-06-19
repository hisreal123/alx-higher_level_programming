#!/usr/bin/node
const sysArg = process.argv.slice(2);

if (sysArg <= 0) {
  console.log("No argument");
} else {
  console.log(sysArg[3]);
}
