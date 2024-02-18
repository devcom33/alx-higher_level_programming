#!/usr/bin/node

const args = process.argv.slice(2);
const numArgs = args.length;

if (numArgs === 0) {
  console.log('No Argument\n');
} else if (numArgs === 1) {
  console.log('Argument found\n');
} else {
  console.log('Arguments found\n');
}
