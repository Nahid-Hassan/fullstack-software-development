const _ = require("underscore");

/**
 * _ is an object; like const _ = {};
 * _.map(list, function(value, index, list) { // code })
 *
 * _.map([1,2,3], function(value, index, list) {console.log(value)})}))
 *
 * difference between map and forEach is map return an array and forEach doesn't return anything.
 */

const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const result = nums.map(function (value, index, list) {
  console.log(value);
  return value * 2; // if not return, it will return undefined
});

console.log(result); // [2,4,6,8,10,12,14,16,18,20]

const weapons = ["rock", "paper", "scissors"];
const makeBroken = weapons.map(function (value) {
  return `Broken ${value}`;
});

console.log(makeBroken); // ['Broken rock', 'Broken paper', 'Broken scissors']

const makeBroken1 = function (item) {
  return `Broken ${item}`;
};
console.log(_.map(weapons, makeBroken1)); // ['Broken rock', 'Broken paper', 'Broken scissors']

/**
 * A tribute to forEach
 */
// const result1 = nums.forEach(function(value, index, list) {
//     console.log(value);
//     return value * 2;
// });
// console.log(result1); // undefined
