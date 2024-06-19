#!/usr/bin/node

const addMeMaybe = (n, theFunction) => {
  n++;
  theFunction(n++);
};

module.exports.addMeMaybe = addMeMaybe;
