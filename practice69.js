// https://www.codewars.com/kata/5202ef17a402dd033c000009/train/javascript

function titleCase(title, minorWords) {
    titleList = title.split(" ").map(word => word.toLowerCase());
    minorWordList = [];
    if (minorWords !== undefined) {
        minorWordList = minorWords.split(" ").map(word => word.toLowerCase());
    }

    function capFirst(word) {
        if (word.length === 0) {
            return word;
        }
        chars = word.split("");
        chars[0] = chars[0].toUpperCase();
        return chars.join("");
    }

    return titleList.map((val, idx) => {
        if (idx === 0) {
            return capFirst(val);
        }
        if (minorWordList.includes(val)) {
            return val;
        }
        return capFirst(val);
    }).join(" ");
}
console.log(titleCase(''))
console.log(titleCase('a clash of KINGS', 'a an the of'))
console.log(titleCase('THE WIND IN THE WILLOWS', 'The In'))
console.log(titleCase('the quick brown fox'))