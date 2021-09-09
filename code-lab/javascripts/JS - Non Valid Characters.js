var box = {};

box['material'] = 'cardboard';
box[0] = 'meow';
box['^&*'] = 'testing 123';

var test = box['^&*'];

console.log(box)
console.log(test)

// inside brackets, everything is stringifyed
box[function () {}] = 'i am alone';
console.log(box);

// immediately invoked function expression, returns the hello
box[(function() {return 'hello'})()] = 'hello dear';
console.log(box);