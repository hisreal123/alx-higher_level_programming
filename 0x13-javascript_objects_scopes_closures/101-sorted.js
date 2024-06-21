#!/usr/bin/node

const { dict } = require('./101-data');
const groupedDict = {};

Object.entries(dict).forEach(([key, value]) => {
  if (groupedDict[value]) {
    groupedDict[value].push(key);
  } else {
    groupedDict[value] = [key];
  }
});

console.log(groupedDict);
