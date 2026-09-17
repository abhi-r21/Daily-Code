/* Predict the Output:
console.log(Boolean(0));
console.log(Boolean(1));
console.log(Boolean(""));
console.log(Boolean("hello")); */

console.log(Boolean(0)); //false
console.log(Boolean(1)); //true
console.log(Boolean("")); //false
console.log(Boolean("Hello")); //true

//Because the non-empty values are always truthy and Emply/zero-like values are always falsy