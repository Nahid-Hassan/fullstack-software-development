let person = {};

// Anything that you ever uses a dot in JavaScript is an object.
// assignment
person.name = "Md. Nahid Hassan Senior";
console.log(person.name); // Md. Nahid Hassan Senior
// same
// console.log(person['name']);

let person1 = {
  name: "Md. Nahid Hassan Junior",
};
console.log(person1.name); //Md. Nahid Hassan Junior

// return
let who = person.name;
console.log(who); // Md. Nahid Hassan Senior

person.name = "Mehedi Hassan Mahin";
// who is stored by value
console.log(who); // Md. Nahid Hassan Senior
console.log(person.name); // Mehedi Hassan Mahin

// primitive(string, number, boolean, null, undefined...) values get pass by value(allocate different place of memory, copy every time)

// non-primitive(object, array, function, promise) values get pass by reference(sharing the same place of memory)

console.log(who.story); // undefined