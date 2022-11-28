#!/usr/bin/node
let argInteger = parseInt(process.argv[2]);
if (isNaN(argInteger)) {
  console.log('Missing number of occurrences');
} else {
  while (argInteger > 0) {
    console.log('C is fun');
    argInteger -= 1;
  }
}
