//https://www.codewars.com/kata/split-the-bill

function splitTheBill(x) {
    let keys = Object.keys(x);
    let totalAmount = keys.reduce((subTotal, person) => subTotal += x[person], 0);
    let avgAmount = totalAmount / keys.length;
    let result = keys.reduce((acc, person) => { 
      acc[person] = x[person] - avgAmount;
      acc[person] = Math.round(acc[person] * 100) / 100;
      return acc; 
      }, {} );
    return result;
}