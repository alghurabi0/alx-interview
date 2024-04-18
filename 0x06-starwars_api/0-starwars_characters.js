#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 2) {
  process.exit(1);
}
let movieId = process.argv[1];
movieId = parseInt(movieId, 10);
if (isNaN(movieId)) {
  process.exit(1);
}
const names = [];
request(
  `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  function (error, response, body) {
    if (error) {
      return;
    }
    const movieData = JSON.parse(body);
    const chars = movieData.characters;
    for (const charUrl in chars) {
      request(charUrl, function (error, response, body) {
        if (error) {
          return;
        }
        const charData = JSON.parse(body);
        names.push(charData.name);
      });
    }
  }
);
for (const name in names) {
  console.log(name);
}
