/**
 * | Falsy     | Truthy           |
 * | --------- | ---------------- |
 * | ""        | "foo"            |
 * | 0,-0      | 23               |
 * | null      | {a: 1}           |
 * | NaN       | [1,2]            |
 * | false     | true             |
 * | undefined | function() {...} |
 */

/**
 * if (true) {
 *  // this block of code execute
 * }
 */

if (studentInputElem.value) {
  numStudents = Number(studentsInputElem.value);
}

/**
 * while (true) {
 *  this block of code execute
 * }
 */

while (newStudents.length) {
  enrollStudent(newStudents.pop());
}

// !newStudents.length
//------ both are same--- 
// newStudents.length > 0

// Note:

// !false -> true
// !!false -> false
// !!!false -> true

