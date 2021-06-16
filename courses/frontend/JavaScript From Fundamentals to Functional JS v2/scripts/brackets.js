let person = [];
person.name = "Md. Nahid Hassan";
let who = person.name;
person[10] = "I am a student.";

console.log(person["10"]); //  "I am a student."
console.log(person[10]); // "I am a student."


console.log(person[]);
// [ <10 empty items>, 'I am a student.', name: 'Md. Nahid Hassan' ]

let age = "age";
person[age] = 23;

console.log(person.age);

console.log(person); // 23

/**
 * [ <10 empty items>,
 * 'I am a student.',
 * name: 'Md. Nahid Hassan',
 * age: 23 ]
 */
