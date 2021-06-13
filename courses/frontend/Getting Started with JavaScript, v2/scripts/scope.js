let teacher = "Nahid";

( function anotherTeacher() {
    let teacher = 'Mahin';
    console.log(teacher); // Mahin
})(); // immediately invoked

console.log(teacher); // Mahin

{
    let teacher = 'Mahin';
    console.log(teacher);
}

console.log(teacher);

function formatStr(str) {
    // prefix and rest only exist in this
    // curly brace.
    {
        let prefix, rest;
        prefix = str.slice(0,3 );
        rest = str.slice(3)
        str = prefix.toUpperCase() + rest;
    }
    // rest of the code
}