#!/usr/bin/node

// 
const fs = require('fs')
const path = require('path')


fs.readFile(process.argv[2], "utf-8", (err, data) => {
  if (err){
    console.log(err)
  } else {
    console.log(data);
  }
});