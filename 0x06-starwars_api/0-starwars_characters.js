#!/usr/bin/node
const request = require("request");
if (process.argv.length != 2) {
  return;
}
let movieId = process.argv[1];
movieId = parseInt(movieId, 10);
if (isNaN(movieId)) {
  return;
}
let names = [];
request(
  `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  function (error, response, body) {
    const movieData = JSON.parse(body);
    const chars = movieData.characters;
    for (const charUrl in chars) {
      request(charUrl, function (error, response, body) {
        const charData = JSON.parse(body);
        names.push(charData.name);
      });
    }
  }
);
for (name in names) {
  console.log(name);
}
