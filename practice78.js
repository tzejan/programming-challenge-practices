//https://www.codewars.com/kata/range-extraction/javascript

function solution(list){
 // TODO: complete solution 
 let pairs = list.reduce((ranges, num) => {
   if (ranges[ranges.length-1] === num - 1){
     ranges[ranges.length-1] = num;
   } else {
     ranges.push(num);
     ranges.push(num);
   }
   return ranges;
   
 }, []);
 
 let result = [];
 for(let idx = 0; idx < pairs.length; idx += 2){
   if (pairs[idx] === pairs[idx+1]){
     result.push(pairs[idx]);
   } else if (pairs[idx+1] - pairs[idx] === 1){
     result.push(pairs[idx])
     result.push(pairs[idx+1]);
   } else {
     result.push(pairs[idx] + '-' + pairs[idx+1])
   }
 }
  return result.join(",");
}