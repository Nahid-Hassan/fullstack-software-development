const game = {};
console.log(game); // {}

game["suspeeta"] = [];
console.log(game); // { "suspeeta": [] }

game.suspeeta.push({
  name: "Rusty",
  color: "Orange",
});

console.log(game); // { "suspeeta": [{ "name": "Rusty", "color": "Orange" }] }

game.suspeeta[1] = {
  name: "Bella",
  color: "Blue",
};

console.log(game.suspeeta); // [{ "name": "Rusty", "color": "Orange" }, { "name": "Bella", "color": "Blue" }]
// console.log(game["suspeeta"]);

/**
 * for (let key in obj) {
 *     console.log(key); // return the key
 * }
 */

console.log("---------------");
for (let property in game) {
  for (let key in game[property]) {
    for (let j in game[property][key]) {
      console.log(game[property][key][j]);
    }
  }
}

/*
Rusty
Orange
Bella
Blue
*/
console.log("---------------");

/**
 * Using destructuring
 */

var [suspeeta, ...rest] = game.suspeeta;
console.log(suspeeta); // { "name": "Rusty", "color": "Orange" }
console.log(rest); // [{ "name": "Bella", "color": "Blue" }]

console.log(game.suspeeta); // [{ "name": "Rusty", "color": "Orange" }, { "name": "Bella", "color": "Blue" }]
const [{ color: color1 }, { color: color2 }] = game.suspeeta; // destructuring
console.log(color1); // Orange
console.log(color2); // Blue



