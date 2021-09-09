var person = [];

person.name = "John";

var who = person.name; // who is John, pass by value

// log who to the console
console.log(who, typeof who); // John string
console.log(person, typeof person); // [object Object] object

person.age = 32; // add age property to person object
person.push(23); // add 23 to the end of the array
console.log(person.name); // John
console.log(person.length); // 1
