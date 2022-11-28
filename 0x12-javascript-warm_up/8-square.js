#!/usr/bin/node
const squareSize = parseInt(process.argv[2]);
if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < squareSize) {
    console.log('X'.repeat(squareSize));
    i++;
  }
}
