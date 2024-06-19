#!/usr/bin/node
const sysArgv = process.argv.slice(2);

// this should work
if (sysArgv.length <= 0) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
