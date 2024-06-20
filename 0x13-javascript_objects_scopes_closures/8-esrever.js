#!/usr/bin/node
exports.esrever = function (list) {
  const tempList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    tempList.push(list[i]);
  }

  return tempList;
};
