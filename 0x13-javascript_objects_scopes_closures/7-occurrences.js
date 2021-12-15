#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const x of list) {
    if (x === searchElement) {
      i++;
    }
  }
  return i;
};
