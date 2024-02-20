#!/usr/bin/node

const args = process.argv.slice(2);
const arg1 = parseInt(args[0]);

if (isNaN(arg1)) {
  console.log('Missing number of occurrence');
} else {
  for (let i = 0; i < arg1; i++) {
    console.log('C is fun');
  }
}
