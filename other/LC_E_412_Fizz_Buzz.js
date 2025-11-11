
/*  Return an n-indexed array where:
    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true. */

// var fizzBuzz = function(n) {
//     let array = []         

//     // Initailize 1-indexed array values: [1, 2, 3, 4, etc.]
//     for (let i = 1; i <= n; i++) {
//         array[i] = i;

//         if (array[i] % 3 === 0 && array[i] % 5 === 0) {
//             array[i] = "FizzBuzz";
//         }
//         else if (array[i] % 3 === 0 && array[i] % 5 !== 0) {
//             array[i] = "Fizz";
//         }
//         else if (array[i] % 3 !== 0 && array[i] % 5 === 0) {
//             array[i] = "Buzz";
//         }
//         else {
//             array[i] = array[i].toString();
//         }

//     }
//     return array;
// };


// Answer variation. Slower execution, but easier to read.
var fizzBuzz = function(n) {
    let array = []         

    // Initailize 1-indexed array values: [1, 2, Fizz, 4, Buzz, etc.]
    for (let i = 1; i <= n; i++) {

        let divisibleBy3 = Boolean(i % 3 === 0);
        let divisibleBy5 = Boolean(i % 5 === 0);
        let currString = "";

        if (divisibleBy3) {
            currString += "Fizz";
        }
        if (divisibleBy5) {
            currString += "Buzz";
        }
        if (currString.length === 0) {
            currString += i;
        }
        array[i-1] = currString;
    }
    return array;
};

num1 = 3
num2 = 5
num3 = 15

console.log(fizzBuzz(num3))