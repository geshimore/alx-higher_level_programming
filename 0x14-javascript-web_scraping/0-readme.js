#!/usr/bin/node

let filename = process.argv[2];
const fs = require('fs');
fs.readFile(filename, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
1-writeme.js 100-starwars_characters.js 2-statuscode.js 3-starwars_title.js 4-starwars_count.js 5-request_store.js 6-completed_tasks.js
