//Create a grade system : 90+ is A, 80-89 is B, 70-79 is C, 60-69 is D, Below 60 is F
// input marks : let marks = 89;

let marks = 89;

if (marks >= 90) {
  console.log("A grade");
} else if (marks >= 80 && marks <= 89) {
  console.log("B grade");
} else if (marks >= 70 && marks <= 79 ) {
  console.log("C grade");
} else if (marks >= 60 && marks <= 69 ) {
  console.log("D grade");
} else {
  console.log("Your fail")
}