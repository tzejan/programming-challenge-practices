//https://www.codewars.com/kata/really-complex-sum/train/javascript

function complexSum(arr){
    const regex = /^((?!(?:(?:[+-]?\d*)i))[-]?\d*)?(([+-]?\d*)i)?$/;
    var realPart = 0;
    var complexPart = 0;
    for (cn of arr){
        m = regex.exec(cn);
        var r = 0;
        var c = 0;
        if (m){
            r = parseInt(m[1]) || 0;
            if (m[2]){
                c = (m[3] && parseInt(m[3])) || ( m[3] === '-' ? -1 : 1 );
            }
        }
        realPart += r;
        complexPart += c;
    }
    answer = '';

    if (!realPart && !complexPart){
        return '0';
    }
    if (realPart){
        answer += realPart;
    }
    if (complexPart){
        if (complexPart < 0){
            answer += '-';
        } else if (answer){
            answer += '+'
        }

        if (Math.abs(complexPart) !== 1){
            answer += Math.abs(complexPart);
        }
        answer += 'i'
    }
    return answer;
}


complex = ["2+3i","3-i"];
console.log(complexSum(complex));
complex = ["10-i","10+i"];
console.log(complexSum(complex));
complex = ["2+3i","-2-3i"];
console.log(complexSum(complex));
complex = ["5"];
console.log(complexSum(complex));
complex = ["i"];
console.log(complexSum(complex));
complex = ["-i"];
console.log(complexSum(complex));
complex = ["3i"];
console.log(complexSum(complex));
complex = [""];
console.log(complexSum(complex));