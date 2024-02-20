#!/usr/bin/node

const args = process.argv.slice(2);

function add (a, b) {
  return a + b;
}

console.log(add(parseInt(args[0]), parseInt(args[1])));
