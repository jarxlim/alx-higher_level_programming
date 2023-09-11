#!/usr/bin/node

let result = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  result = args[args.length - 2];
}
console.log(result);
