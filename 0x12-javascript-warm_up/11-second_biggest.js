#!/usr/bin/node

const args = process.argv.slice(2);
const numArgs = args.length;

for(let i in args.sort()) {
  console.log(`${args[i]}`);
}
