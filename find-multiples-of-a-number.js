// https://www.codewars.com/kata/58ca658cc0d6401f2700045f

function findMultiples(integer, limit) {
    //your code here
    var result = [];

    for (var i = integer; i <= limit; i += integer) {
        result.push(i);
    }
    return result;
}