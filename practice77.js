//https://www.codewars.com/kata/break-camelcase/javascript

function solution(string) {
    return string.split("").map(char => /[A-Z]/.test(char) ? " " + char : char).join("");
}