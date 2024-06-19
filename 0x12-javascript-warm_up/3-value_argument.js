#!/usr/bin/node
const sysArg = process.argv;

if (sysArg <= 2) {
  console.log("No argument");
} else {
  console.log(sysArg[3]);
}
