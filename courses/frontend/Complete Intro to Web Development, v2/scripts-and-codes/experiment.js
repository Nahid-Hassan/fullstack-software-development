// return everything that has class .js-target in one array object.
const elementsToChange = document.querySelectorAll(".js-target");

// Iteratively process every element that has .js-target class
// method -1
for (let i = 0; i < elementsToChange.length; i++) {
  const currentElement = elementsToChange[i];
  currentElement.innerText = "Modified by JavaScript";
  currentElement.style.color = "red";
}

// method -2, less code, this the part of js functional programming
// elementsToChange.forEach(function (element) {
//     element.innerText = 'ForEach'
// })

const button = document.querySelector(".event-button");
button.addEventListener("click", function () {
  alert("Hey there!");
});

const input = document.querySelector('.input-to-copy');
const paragraph = document.querySelector('.p-to-copy-to');

input.addEventListener('keyup', function() {
    paragraph.innerText = input.value
});