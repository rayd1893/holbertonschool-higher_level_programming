#!/usr/bin/node
const list = require('./100-data').list;

const map1 = list.map((element, index) => { return element * index; });
console.log(list);
console.log(map1);
