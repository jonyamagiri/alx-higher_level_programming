#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];

try {
  const content = fs.readFileSync(filename, 'utf-8');
  console.log(content);
} catch (error) {
  console.error(error.message);
}
