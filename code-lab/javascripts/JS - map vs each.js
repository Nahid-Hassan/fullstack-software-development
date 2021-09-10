const _ = require("underscore");

function createSuspectObjects(name) {
  return {
    name: name,
    color: name.split(" ")[1],
    speak() {
      console.log("My name is " + this.name + ".");
    },
  };
}

var suspects = [
  "Miss Scarlet",
  "Colonel Mustard",
  "Mrs. White",
  "Mrs. Peacock",
  "Professor Plum",
];

/**
 * using _.map() to create an array of suspect objects
 */

const suspectsList = _.map(suspects, function (name) {
  return createSuspectObjects(name);
});
console.log(suspectsList);

// same as above
// const suspectsList2 = suspects.map((name) => { return createSuspectObjects(name); });

/**
 * using _.each() 
 */

_.each(suspectsList, (name) => {
    name.speak();
})