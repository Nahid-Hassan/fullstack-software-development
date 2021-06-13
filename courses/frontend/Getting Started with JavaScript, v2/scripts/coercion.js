let msg1 = 'There are '
let numStudents = 20
let msg2 = " students."

// type -1
console.log(msg1 + numStudents + msg2);
// "There are 20 students."


// type -2
console.log(`There are ${numStudents} students.`);



// function
function addStudent(numStudents) {
    return numStudents + 1;
}

// DOM return value/number as string
// call addStudent()
// Number(string) // convert string to a number
addStudent(Number(studentsInputElem.value));
// 12