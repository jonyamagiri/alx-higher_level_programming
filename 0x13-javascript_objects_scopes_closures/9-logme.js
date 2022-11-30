#!/usr/bin/node

let numberArgs = 0;
exports.logMe = function (item) {
  console.log(numberArgs + ': ' + item);
  numberArgs += 1;
};
