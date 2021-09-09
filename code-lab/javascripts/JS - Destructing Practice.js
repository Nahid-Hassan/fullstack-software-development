/**
 * Destructuring Array
 */

// Normal
var [a, b] = [1, 2];
console.log(a, b);

// Omit certain values
var [a, , c] = [1, 2, 3];
console.log(a, c); // 1 2 3

// Combine with rest operator (...)
var [a, ...b] = [1, 2, 3, 4, 5];
console.log(a, b); // 1 [2, 3, 4, 5]

// swap variables easily without temp variable
var [a, b] = [1, 2];
[a, b] = [b, a]; // swap a and b
console.log(a, b); // 2 1

// advanced nesting destructuring
var [a, [b, c]] = [1, [2, 3]];
console.log(a, b, c); // 1 2 3

var [a, [b, [c, d]]] = [1, [2, [[[3, 4], 5], 6]]];
console.log(a, b, c, d); // a: 1 b: 2 c: [[ 3, 4 ], 5 ] d: 6

// Object destructuring
var { user: x } = { user: "John" };
console.log(x); // John
