// https://www.codewars.com/kata/find-count-of-most-frequent-item-in-an-array/train/javascript

function mostFrequentItemCount(collection) {
  // Do your magic. :)
  let counts = collection.reduce((counts, num) => { 
    counts[num] = (counts[num] || 0) + 1 ;
    return counts;
  }, []);  
  return Object.keys(counts).reduce((highest, key) => 
    counts[key] > highest? counts[key] : highest,
    0);