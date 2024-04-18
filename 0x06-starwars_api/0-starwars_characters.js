#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 3) {
  process.exit(1);
}
let movieId = process.argv[2];
movieId = parseInt(movieId, 10);
if (isNaN(movieId)) {
  process.exit(1);
}
request(
  `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  async function (error, response, body) {
    if (error) {
      console.log('movie req error', error);
      return;
    }
    const movieData = JSON.parse(body);
    const chars = movieData.characters;
    for (const charUrl of Object.values(chars)) {
      const name = await new Promise((resolve, reject) => {
        request(charUrl, function (error, response, body) {
          if (error) {
            reject(error);
          } else {
            const charData = JSON.parse(body);
            resolve(charData.name);
          }
        });
      });
      console.log(name);
    }
  }
);
