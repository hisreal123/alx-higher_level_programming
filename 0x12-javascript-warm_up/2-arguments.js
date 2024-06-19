#!/usr/bin/node
const sysArgv = process.argv.slice(2);

if (sysArgv.length <= 0) {
  console.log('No argument');
} else if (sysArgv.length <= 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
