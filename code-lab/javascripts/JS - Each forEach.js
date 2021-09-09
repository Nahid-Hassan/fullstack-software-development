var _ = require('underscore');


// @ts-check
function createSuspectObject(name) {
  return {
    name: name,
    color: name.split(" ")[1],
    speak() {
      console.log("My name is " + this.name + ".");
    },
  };
}

var suspects = ["Miss Scarlet", "Colonel Mustard", "Mr. White"];

var suspectsList = [];

// call createSuspectObject for each suspect

_.each(suspects, function(name) {
  suspectsList.push(createSuspectObject(name));
});

// suspects.forEach((name, key, value) => { // key, value are optional
//   // console.log(name, key, value); // "Miss Scarlet", 0, ["Miss Scarlet", "Colonel Mustard", "Mr. White"]
//   suspectsList.push(createSuspectObject(name));
// });

console.log(suspectsList);

/**
 * _.each(array, function(currentValue, index, array) {
 *  // ...
 * });
 * 
 * iterable.forEach(function(currentValue, index, array) {
 * // ...
 * });
 */

