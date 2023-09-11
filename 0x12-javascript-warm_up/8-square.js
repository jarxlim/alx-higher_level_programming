#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);
  if (!isNaN(size)) {
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  } else {
    console.log('Missing size');
  }
}
