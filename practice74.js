// https://www.codewars.com/kata/most-frequent-elements/python
// python problem, but coded in javascript

function find_most_frequent(arr){
    let histogram = arr.reduce((his, num) => {
        his[num] = his[num]? his[num] + 1 : 1;
        return his;
    }, {})
    let highest = Object.values(histogram).reduce((highest, val) => val > highest? val:highest, 0);
    return Object.keys(histogram).filter( key => histogram[key] === highest).map( n => parseInt(n));
}
console.log(find_most_frequent([1, 1, 2, 2, 3]));

// Test.assert_equals(find_most_frequent([1, 1, 2, 3]), set([1]), 'one most frequent element')
// Test.assert_equals(find_most_frequent([1, 1, 2, 2, 3]), set([1, 2]), 'two most frequent element')
// Test.assert_equals(find_most_frequent([]), set([]), 'empty')