#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, async (error, response, body) => {
  if (error) console.log(error);

  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    try {
      const response = await new Promise((resolve, reject) => {
        request.get(character, (error, response, body) => {
          if (error) reject(error);
          resolve(JSON.parse(body).name);
        });
      });
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
});
