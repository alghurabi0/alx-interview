#!/usr/bin/node
const request = require("request");
if (process.argv.length !== 2) {
  console.log("length args error", process.argv);
  process.exit(1);
}
let movieId = process.argv[1];
movieId = parseInt(movieId, 10);
if (isNaN(movieId)) {
  console.log("int str argv error", movieId);
  process.exit(1);
}
const names = [];
request(
  `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  function (error, response, body) {
    if (error) {
      console.log("movie req error", error);
      return;
    }
    console.log("body", body);
    console.log("response", response);
    const movieData = JSON.parse(body);
    console.log("movieData", movieData);
    const chars = movieData.characters;
    for (const charUrl in chars) {
      request(charUrl, function (error, response, body) {
        if (error) {
          console.log("char error", error);
          return;
        }
        console.log("body", body);
        console.log("response", response);
        const charData = JSON.parse(body);
        console.log("charData", charData);
        names.push(charData.name);
      });
    }
  }
);
console.log(names);
for (const name in names) {
  console.log(name);
}
