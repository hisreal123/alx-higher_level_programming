#!/usr/bin/node
// a script to write a string into a file

const fs = require("fs");
const path = require("path");

fs.writeFile(process.argv[0], "Python is cool", "utf8", (err) =>
  err ? console.log(err) : null
);
