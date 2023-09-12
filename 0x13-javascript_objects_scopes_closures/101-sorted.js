#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDic = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (newDic[dict[occurences]] === undefined) {
    newDic[dict[occurences]] = [occurences];
  } else {
    newDic[dict[occurences]].push(occurences);
  }
});
console.log(newDic);
