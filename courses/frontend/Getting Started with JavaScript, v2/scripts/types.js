let v;
console.log(typeof v); // undefined

v = "1"
console.log(typeof v); // string

v = 2
console.log(typeof v); // number

v=true
console.log(typeof v); // boolean

v={}
console.log(typeof v); // object

v = Symbol()
console.log(typeof v); // symbol

console.log(typeof huda); // undefined

v = null
console.log(typeof v); // object


v = function() {}
console.log(typeof v); // function

v = [1,2,3]
console.log(typeof v); // object
