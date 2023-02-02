#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request.get(url, async (error, response, body) => {
  if (error) console.log(error);

  for (const character of JSON.parse(body).characters) {
    request.get(character, (error, response, body) => {
      if (error) console.log(error);
      console.log(JSON.parse(body).name);
    });
  }
});
