#!/usr/bin/node
const sysArgv = process.argv;

if (sysArgv.length <= 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
