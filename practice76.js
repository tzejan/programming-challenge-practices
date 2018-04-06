//https://www.codewars.com/kata/directions-reduction/javascript

function dirReduc(arr){
  // ...
  let result = arr.slice();
  let reduced = true;
  const lookup = {
  "NORTH": "SOUTH",
  "SOUTH": "NORTH",
  "EAST": "WEST",
  "WEST": "EAST"
  }
  while (reduced){
    reduced = false;
    let input = result.slice();
    result = [];
    
    for (let idx = 0; idx < input.length; idx++){
      if (idx === input.length-1){
        result.push(input[idx]);
        continue;
      }
      if (lookup[input[idx]] === input[idx+1]){
        idx++;
        reduced = true;
        continue;
      }
      result.push(input[idx]);
    }
  }