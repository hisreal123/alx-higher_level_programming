#!/usr/bin/node
// a script that prints all characters of a Star Wars movie

const req = require("request");
const id = process.argv[2];
const url = "https://swapi-api.hbtn.io/api/films/";
req.get(url + id, function (error, _res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    req.get(i, function (error, _res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
