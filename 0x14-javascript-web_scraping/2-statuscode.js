#!/usr/bin/node
// A script that display the status code of a GET request.

const request = require('request');
request.get(process.argv[2], (err, response) => {
  err ? console.log(err) : console.log('code: ' + response.statusCode);
});
