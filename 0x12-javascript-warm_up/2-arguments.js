#!/usr/bin/node
const sysArgv = process.argv.slice(2);

if (sysArgv.length <= 0) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
