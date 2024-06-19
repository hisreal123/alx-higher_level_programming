#!/usr/bin/node

const sysArg = process.argv.slice(2);
const arg1 = sysArg[0];

const parseInteger = (arg1) => {
  if (!parseInt(arg1)) {
    console.log('Not a number');
  } else if (parseInt(arg1)) {
    console.log(`My number: ${parseInt(arg1)}`);
  } else {
    return null;
  }
};

parseInteger(arg1);
