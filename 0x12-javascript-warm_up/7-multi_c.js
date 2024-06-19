#!/usr/bin/node

const sysArg = process.argv.slice(2);
const arg1 = sysArg[0];

const MultipleOccurences = (arg1) => {
  if (!parseInt(arg1)) {
    console.log('Missing number of occurrences');
  } else if (parseInt(arg1)) {
    const value = parseInt(arg1);
    // for (let i = 0; i < value; i++){
    //     console.log("C is fun");
    // }
    let i = 0;
    while (i < value) {
      console.log('C is fun');
      i++;
    }
  } else {
    return null;
  }
};

MultipleOccurences(arg1);
