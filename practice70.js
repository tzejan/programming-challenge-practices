//https://www.codewars.com/kata/decode-the-morse-code/javascript

decodeMorse = function(morseCode){
  return morseCode.trim().replace(/\s{3}/g, " | ").split(" ").map( val => {
    return (val === "|")? " " : MORSE_CODE[val];
  }).join("");
}