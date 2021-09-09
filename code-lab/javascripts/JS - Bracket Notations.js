var person = [];
var plea = 'wouldShe';

person.name = "Mrs. White";
person[plea] = "I would never";

// log person
console.log(person);
// log person length
console.log(person.length);
// log person plea using bracket notation
console.log(person[plea]); // I would never
// log person plea using dot notation
console.log(person.plea); // undefined
// log person plea using dot notation
console.log(person.wouldShe); // I would never


person[age] = 30; // age is not defined

// person.0; // error