#!/usr/bin/node
// concats 2 files

const fs = require('fs');
const argOne = fs.readFileSync(process.argv[2], { encoding: 'utf8' });
const argTwo = fs.readFileSync(process.argv[3], { encoding: 'utf8' });
fs.writeFileSync(process.argv[4], argOne + argTwo);

/*
// concats 2 files

const fs = require('fs');
const argOne = fs.readFileSync(process.argv[2], 'utf8');
const argTwo = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], argOne + argTwo);
*/
