#!/usr/bin/node

const countx = 0;

exports.logMe = function countx (item) {
  console.log(`${countx}: ${item}`);
  countx += 1;
};
