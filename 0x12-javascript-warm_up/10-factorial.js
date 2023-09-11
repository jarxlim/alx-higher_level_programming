#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Factorial of NaN is 1');
} else {
  const number = parseInt(process.argv[2]);
  if (!isNaN(number)) {
    function factorial (n) {
      if (n <= 1) {
        return 1;
      } else {
        return n * factorial(n - 1);
      }
    }
    const result = factorial(number);
    console.log(`Factorial of ${number} is ${result}`);
  } else {
    console.log('Factorial of NaN is 1');
  }
}
