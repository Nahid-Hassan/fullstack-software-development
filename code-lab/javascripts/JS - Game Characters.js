var game = {}; // game object

game.mudderer = "??";
game["weapons"] = [
    { type: "lasers", location: "lab"},
    { type: "angry cats", location: "room 1"}, 
    { type: "dish soap", location: "kitchen"}];


game.name = [];
game.name[0] = "John";
game.name.push("Mary");

console.log(game.weapons[0].type); // lasers
console.log(game.name); // John, Mary
console.log(game); // {mudderer: ??, weapons: [{type: "lasers", location: "lab"}, {type: "angry cats", location: "room 1"}, {type: "dish soap", location: "kitchen"}], name: Array[2]}

