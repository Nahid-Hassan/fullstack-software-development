function createSuspectObject(name) {
  return {
    name: name,
    color: name.split(" ")[1],
    // speak: function () {
    //   console.log("My name is " + this.name + ".");
    // },
    speak() {
      console.log("My name is " + this.name + ".");
    },
  };
}

var suspects = ["Miss Scarlet", "Colonel Mustard", "Mr. White"];

var suspectList = [];

for (const suspect of suspects) {
  suspectList.push(createSuspectObject(suspect));
}

console.log(suspectList);
suspectList[0].speak();
