#!/usr/bin/node
const [,, arg1] = process.argv;

if (!arg1) {
  console.log('No argument');
} else {
  console.log(arg1);
}
