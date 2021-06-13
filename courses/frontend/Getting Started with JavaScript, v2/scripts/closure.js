function f1(a) {
    let b = 2;

    setTimeout(function() {
        console.log(a, b)
    }, 1000);
}

f1(10)