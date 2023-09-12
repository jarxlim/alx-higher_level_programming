#!/usr/bin/node
const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

if (
  fs.existsSync(file1) &&
fs.statSync(file1).isFile &&
fs.existsSync(file2) &&
fs.statSync(file2).isFile &&
file3 !== undefined
) {
  const file1Content = fs.readFileSync(file1);
  const file2Content = fs.readFileSync(file2);
  const stream = fs.createWriteStream(file3);

  stream.write(file1Content);
  stream.write(file2Content);
  stream.end();
}
