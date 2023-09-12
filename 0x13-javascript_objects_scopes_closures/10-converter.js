#!/usr/bin/node

exports.converter = function (base) {
  function Converter (n) {
    return n.toString(base);
  }

  return Converter;
};
