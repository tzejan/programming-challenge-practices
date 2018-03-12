// https://www.codewars.com/kata/56747fd5cb988479af000028

// You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

function getMiddle(s)
{
  let halfLength = Math.floor(s.length / 2);
  let startingIndex = halfLength;
  if (s.length % 2 === 0){
    startingIndex -= 1;
  }
  return s.slice(startingIndex, halfLength+1); 
}