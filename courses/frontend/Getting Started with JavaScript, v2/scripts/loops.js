let students = {
  /*....*/
};

// method -1
for (let i = 0; i < students.length; i++) {
  greetStudent(students[i]);
}

// method -2
for (let student of students) {
  greetStudent(student);
}

// while loop

while (students.length > 0) {
  let student = students.pop();
  greetStudent(student);
}
