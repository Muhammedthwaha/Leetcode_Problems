// converting the number to a string
function isPalindrome(num) {
    let word = String(num);
    let reversedWord = "";

    for (let i = word.length - 1; i >= 0; i--) {
        reversedWord += word[i];
    }
    return word === reversedWord;
}
//Test Cases
console.log(isPalindrome(10));   // false
console.log(isPalindrome(121));  // true
console.log(isPalindrome(-121)); // false



// Without converting the number to a string
// function isPalindrome(num) {
//     if (num < 0) {
//         return false; // Negative numbers are not palindromes
//     }
//      let originalNum = num;
//      let reversedNum = 0;

//      while (num > 0) {
//         const digit = num % 10; // Get the last digit
//         reversedNum = reversedNum * 10 + digit;
//         num = Math.floor(num / 10); // Remove the last digit
//         }
//     return originalNum === reversedNum; // Check if the original number is equal to the reversed number
    
// }

// //Test Cases
// console.log(isPalindrome(121));  // true
// console.log(isPalindrome(-121)); // false
// console.log(isPalindrome(10));   // false
