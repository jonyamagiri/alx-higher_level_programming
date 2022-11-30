#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};

/*
exports.esrever = function (list) {
  const reversedList = [];
  let i = list.length - 1;
  while (i >= 0) {
    reversedList.push(list[i]);
    i -= 1;
  }
  return reversedList;
};
*/
