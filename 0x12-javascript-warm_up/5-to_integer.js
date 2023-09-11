#!/usr/bin/node

const arg = process.argv;
const num = parseInt(arg[2], 10);

if (isNaN(num)) {
  cosole.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
