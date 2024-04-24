#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      return;
    }
    const concatenatedData = dataA + dataB;
    fs.writeFile(fileC, concatenatedData, (err) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(`Files ${fileA} and ${fileB} successfully concatenated into ${fileC}`);
    });
  });
});
