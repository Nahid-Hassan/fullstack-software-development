// example - 1
function ask(question) {
  let teacher = "nahid";
  // this.teacher is not nahid
  // it is mahin
  console.log(this.teacher, question);
  console.log(teacher);
  console.log(this.teacher);
}

function otherClass() {
  var myContext = {
    teacher: "mahin",
  };
  ask.call(myContext, "why"); // call from here
}
otherClass();

// example - 2
let workshop = {
  teacher: "Nahid",
  ask(question) {
    console.log(this.teacher, question);
  },
};

/**
 * None of the line is important, it is only important line
 * workshop.ask(.....), this determined what the this keyword
 * referred.
 */

workshop.ask("what is implicit binding");
// Nahid what is implicit binding.

// example - 1
function ask(question) {
  let teacher = "nahid";
  console.log(this.teacher, question);
}

function otherClass() {
  var myContext = {
    teacher: "mahin",
  };
  //   difference is here
  ask.call(myContext, "why"); // call from here
}
otherClass();

// example - 1
function ask(question) {
  let teacher = "nahid";
  console.log(this.teacher, question);
}

function otherClass() {
  var myContext = {
    teacher: "mahin",
  };
  // difference is here
  ask(myContext, "why"); // call from here
}
otherClass();
