const myDate = new Date();
document.getElementById("demo").innerHTML = isDate(myDate);

function isDate(myDate) {
    console.log(myDate.constructor.toString());
    return myDate.constructor.toString().indexOf("Date") > -1;
}
