// https://www.codewars.com/kata/decode-the-morse-code-advanced


const decodeBits = function(bits){
    // ToDo: Accept 0's and 1's, return dots, dashes and spaces
    const trimmedBits = trimEnds(bits);
    const bitRate = getBitRate(trimmedBits);
    console.log(bitRate);

    reducedMorse = reduceMorseCode(trimmedBits, bitRate);
    let morse = reducedMorse
              .replace(/0000000/g, '   ')
              .replace(/111/g, '-')
               .replace(/000/g, ' ')
              .replace(/1/g, '.')
              .replace(/0/g, '');
    return morse;
}

function getBitRate(bits){
  // let result = Math.min(...bits.match(/0+|1+/g).map(g => g.length));
  // console.log(result);
  // //console.log(Math.min(...result));
  return Math.min(...bits.match(/0+|1+/g).map(g => g.length));
}

function trimEnds(bits){
  return bits.replace(/^0+|0+$/g,'');
}


function reduceMorseCode(bits, rate){
  let result = [];
  for (let i = 0; i < bits.length; i+= rate){
    result.push(bits[i]);
  }
  return result.join("");
}

decodeMorse = function(morseCode){
  return morseCode.trim().split("   ").map( word => word.split(" ").map( char => MORSE_CODE[char] ).join("")).join(" ");
}


//let decodedBits = decodeBits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011');
let decodedBits = decodeBits('00011100010101010001000000011101110101110001010111000101000111010111010001110101110000000111010101000101110100011101110111000101110111000111010000000101011101000111011101110001110101011100000001011101110111000101011100011101110001011101110100010101000000011101110111000101010111000100010111010000000111000101010100010000000101110101000101110001110111010100011101011101110000000111010100011101110111000111011101000101110101110101110')
// let decodedMorse = decodeMorse(decodedBits)
