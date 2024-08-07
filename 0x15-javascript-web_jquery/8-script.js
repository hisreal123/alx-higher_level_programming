#!/usr/bin/node
/* global $ */
// a JavaScript script that fetches and lists the title for all movies by using this
// URL: https://swapi-api.alx-tools.com/api/films/?format=json
$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
    const movies = data.results;
    movies.forEach(movie => {
      $('#list_movies').append(`<li>${movie.title}</li>`);
    });
  });
});
