// declare a object person
var person = {};
person.name = 'John';
person.age = 30;

let who = person.name; // pass by value
let howOld = person.age; // pass by value
let anotherPerson = person; // pass by reference

console.log(who, typeof who);
console.log(howOld, typeof howOld);
console.log(anotherPerson, typeof anotherPerson);

// change in person object effect the anotherPerson object, but not for who and howOld
person.name = 'Jane';

console.log(who);
console.log(howOld);
console.log(anotherPerson);

// now if i defined person object like this
// previous person object is fully changed
person = {
    name: 'Jane Alom',
}

console.log(person); // just show name property, other property is gone

// now add age property to person object
person.age = 25;

// log the person object
console.log(person);

// are you understand the effect? 