#!/usr/bin/node

exports.esrever = function (list) {
  const reve = [];
  for (let i = 0; i < list.length; i++) {
    reve.unshift(list[i]);
  }
  return reve;
};
