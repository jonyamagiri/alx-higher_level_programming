#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

const handleCharacterResponse = (error, response, body) => {
  if (error) console.log(error);
  else console.log(JSON.parse(body).name);
};

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    JSON.parse(body).characters.forEach(character => {
      request.get(character, handleCharacterResponse);
    });
  }
});
