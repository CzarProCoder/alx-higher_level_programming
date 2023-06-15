#!/usr/bin/node

exports.esrever = function (list) {
  const nlist = [];
  let length = list.length - 1;
  while (length >= 0) {
    nlist.push(list[length]);
    length--;
  }
  return nlist;
};
