#!/usr/bin/node
/* global $ */
// a JavaScript script that fetches the character name from this
// URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    $('#hello').text(data?.hello);
  });
});
