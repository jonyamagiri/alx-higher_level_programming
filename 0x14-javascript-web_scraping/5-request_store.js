#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, content) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, content, 'utf-8', writeError => {
      if (writeError) {
        console.log(writeError);
      }
    });
  }
});
