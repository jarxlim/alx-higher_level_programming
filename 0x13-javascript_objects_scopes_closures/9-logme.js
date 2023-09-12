#!/usr/bin/node

let countx = 0;

exports.logMe = function (item) {
  console.log(countx + ': ' + item);
  countx += 1;
};
