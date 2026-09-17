/* Predict the Output:
console.log(5 == "5");, console.log(5 === "5"); 
Expected Output: (TRUE, FALSE) */

// I think the output for the console.log( 5 == "5") is true , because "==" convert the string to number .   
console.log( 5 == "5"); //True

// I think the output for the console.log( 5 === "5") is false , because " === " is strictly equal to it does not convert string into a number because it compares value AND string .
console.log(5 === "5"); //False