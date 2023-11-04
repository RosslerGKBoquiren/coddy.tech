function substitution(key, message) {
    // Write your code below this line
    
}function substitution(key, message) {
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // You can also include lowercase letters if needed
  let encryptedMessage = "";

  for (let i = 0; i < message.length; i++) {
    const char = message[i];
    const charIndex = alphabet.indexOf(char.toUpperCase());

    if (charIndex !== -1) {
      // Check if the character is a letter
      const isUpperCase = char === char.toUpperCase();
      const encryptedChar = isUpperCase ? key[charIndex] : key[charIndex].toLowerCase();
      encryptedMessage += encryptedChar;
    } else {
      // Keep special characters as is
      encryptedMessage += char;
    }
  }

  return encryptedMessage;
}