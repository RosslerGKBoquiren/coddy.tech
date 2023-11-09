function validateCard(cardNumber) {
    // Write your code below this line
  const cardLength = cardNumber.toString().length;
  
  if (cardLength !== 15 && cardLength !== 16) {
    console.log("INVALID");
    return;
  }

  let sum = 0;
  let isSecond = false;
  let tempCardNumber = cardNumber;

  while (tempCardNumber > 0) {
    let digit = tempCardNumber % 10;
    
    if (isSecond) {
      digit *= 2;
      if (digit > 9) {
        digit = digit - 9;
      }
    }

    sum += digit;
    isSecond = !isSecond;
    tempCardNumber = Math.floor(tempCardNumber / 10);
  }

  if (sum % 10 !== 0) {
    console.log("INVALID");
    return;
  }

  let startingDigits = Math.floor(cardNumber / Math.pow(10, cardLength - 2));
  
  if ((cardLength === 15 && (startingDigits === 34 || startingDigits === 37)) ||
      (cardLength === 16 && startingDigits >= 51 && startingDigits <= 55)) {
    if (cardLength === 15) {
      console.log("AMEX");
    } else {
      console.log("MASTERCARD");
    }
  } else {
    console.log("INVALID");
  }
}