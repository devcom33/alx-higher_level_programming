#!/usr/bin/node

const args = process.argv.slice(2);
const arg1 = parseInt(args[0]);

function factoriel (arg1) {
  if (arg1 === 0 || isNaN(arg1) || arg1 === 1) { return 1; }
  return arg1 * factoriel(arg1 - 1);
}
console.log(factoriel(arg1));
