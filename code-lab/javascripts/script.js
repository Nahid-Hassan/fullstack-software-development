const myObj = {
  name: 'John',
  age: 30,
  cars : [
    {name: 'Ford', models: ['Fiesta', 'Focus', 'Mustang']},
    {name: 'BMW', models: ['320', 'X3', 'X5']},
    {name: 'Fiat', models: ['500', 'Panda']}
  ]
}

myObj.details = function() {
  return `${this.name} is ${this.age} years old`.toUpperCase();
}


let x = ""
for (let i in myObj.cars) {
  x += "<h2>" + myObj.cars[i].name + "</h2>"
  for (let j in myObj.cars[i].models) {
    x += myObj.cars[i].models[j] + "<br>"
  } 
}

document.getElementById('demo').innerHTML = x

console.log(myObj.details());