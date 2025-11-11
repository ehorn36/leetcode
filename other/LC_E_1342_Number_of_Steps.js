/*  Given an integer num, return the number of steps to reduce it to zero.
    In one step, if the current number is even, you have to divide it by 2, 
    otherwise, you have to subtract 1 from it. */

var numberOfSteps = function(num) {
    let steps = 0
    let currValue = num;

    while (currValue !==0) {
        if (currValue % 2 === 0) {
            currValue = (currValue / 2);
        }
        else {
            currValue -= 1;
        }
        steps += 1;
    }

    return steps;
};

num1 = 14;
num2 = 8;
num3 = 123;

console.log(numberOfSteps(num3));