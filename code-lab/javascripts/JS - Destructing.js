// destructing
/**
 * Array Destructuring - Order is important.
 */

const [first, second] = ["John", "Doe"];
console.log(first, second); // John Doe
// let [first, second] = ['John', 'Doe'];
// var [first, second] = ['John', 'Doe'];
[third, forth] = ["Jane", "Doe"];
console.log(third, forth); // Jane Doe

// Object.freeze()
const person = {
  name: "John",
  age: 30,
};

console.log(person);
person.name = "Tina";
console.log(person);

// freeze
Object.freeze(person);
person.name = "changed";
console.log(person);

/**
 * Object Destructuring - Order is not important.
 */

myObj = {
    first1: "John",
    second1: "Jane",
}

// const {first1, second1} = {second1: 234, first1: "John"}; // same as below
const {first1, second1} = myObj; // same as above
console.log(first1, second1); // John 234

// Exercise

// solution - 1
const murderer = {
  name: "Rusty",
  room: "Kitchen",
  weapon: "candlestick",
};

const { handle, room, weapon } = murderer;

// log name, room and weapon
console.log(handle, room, weapon);
