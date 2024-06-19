#!/usr/bin/node

const addMeMaybe = (n, theFunction) => {
  n++;
  theFunction();
};

module.exports.addMeMaybe = addMeMaybe;
