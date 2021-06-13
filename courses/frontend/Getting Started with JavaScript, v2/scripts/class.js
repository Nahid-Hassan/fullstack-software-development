class Workshop {
  constructor(teacher) {
    this.teacher = teacher;
    console.log(this.teacher);
  }
  ask(question) {
    console.log(this.teacher, question);
  }
}

let deepJS = new Workshop("Nahid");
let reactJS = new Workshop("Mahin");

deepJS.ask("Something...");
reactJS.ask("Anything...");

console.log(reactJS.teacher); // lokkhipur
console.log(deepJS.teacher); //
