const _ = {};

_.each = function(list, callback) {
    console.log(list);
    console.log(callback);
    if (Array.isArray(list)) {
        // loop through the array
        for (let i = 0; i < list.length; i++) {
            callback(list[i], i, list);
        }
    } else {
        // loop through the object
        for (let key in list) {
            callback(list[key], key, list);
        }
    }
};

_.each(['nahid', 'hasan', 'mony'], function(name, index, list) {
    if (list[index + 1]) {
        console.log(`${name} is next to ${list[index + 1]}`);
    } else {
        console.log(`${name} is last in the list`);
    }
});  