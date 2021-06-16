// declare an array object
let person = [];

// add an array property
person.name = "Md. Nahid Hassan.";

// retrieve array property
let who = person.name;
console.log(who); // Md. Nahid Hassan

// see the type of the person
console.log(typeof person); // object

// add some data into the array
for (let i = 0; i < 10; i++) {
  person[i] = i * 10;
}
console.log(person); // [ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, name: 'Md. Nahid Hassan.' ]

// array length property
console.log(person.length);

person.forEach(element => {
    console.log(element);
    // print out 0\n-90\n
});