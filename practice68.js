//https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/javascript

function divisors(integer) {
    halfNum = Math.floor(integer / 2);
    answers = [];
    for (var i = 2; i <= halfNum; i += 1) {
        if (integer % i === 0) {
            answers.push(i);
        }
    }

    if (answers.length > 0) {
        return answers;
    }
    return integer + ' is prime';
};

console.log(divisors(15));
console.log(divisors(12));

console.log(divisors(13));
console.log(Math.sqrt(15));