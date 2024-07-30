#!/usr/bin/node
// a script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, data) => {
  if (err) {
    console.log(err);
  }
  const movie = JSON.parse(data.body);
  console.log(movie.title);
});
