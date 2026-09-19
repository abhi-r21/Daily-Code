//Count how many numbers between 1 and 100 are divisible by 7.

let num = 7;
let count = 0;

for(let i = 1; i <= 100; i++) {
  if (i % num == 0) {
  count = count + 1;
  }
}

console.log(count);