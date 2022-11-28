#!/usr/bin/node
const numberArg = parseInt(process.argv[2], 10);
if (isNaN(numberArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numberArg);
}
