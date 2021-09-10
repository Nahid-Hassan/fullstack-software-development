/**
 * Note
 * ====================================================================
 * Firstly it take time to understand. So keep your patient. Thank you.
 * ====================================================================
 */

 const _ = {};

 _.map = function (list, callback) {
   var storage = [];
 
   //   for (let i = 0; i < list.length; i++) {
   //     storage.push(callback(list[i], i, list));
   //   }
 
   /**
    * Functional programmer don't like loops. use _.each() instead
    */
   _.each(list, (element, index, list) => {
     storage.push(callback(element, index, list));
   });
 
   return storage;
 };
 
 _.each = function (list, callback) {
   if (Array.isArray(list)) {
     for (let i = 0; i < list.length; i++) {
       callback(list[i], i, list);
     }
   } else {
     for (let key in list) {
       callback(list[key], key, list);
     }
   }
 };
 
 const out = _.map([1, 2, 4], function (num) {
   return num * 2;
 });
 console.log(out); // [2, 4, 8]
 
 console.log(_); // { map: [Function], each: [Function] }
 
 /**
  * Understand some confusion
  * We have a function that contains 1 parameter, but we pass 3 arguments. what happend?
  */
 
 function yourName(name) {
   console.log(arguments); // [Arguments] { '0': 'John', '1': 30, '2': [ 1, 2, 4 ] }
   console.log(`My name is ${name}.`);
 }
 
 yourName("John", 30, [1, 2, 4]);
 