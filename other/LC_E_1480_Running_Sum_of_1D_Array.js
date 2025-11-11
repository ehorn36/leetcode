// Return the running sum of nums:
// var runningSum = function(nums) {

//     // Instantiate return array with the first value of the nums array.
//     let array = [nums[0]]

//     // Begin the loop at index 1, since index 0 is already given. 
//     for (let i = 1; i < nums.length; i++) {
//         array.push(nums[i] + array[i-1]);
//     }

//     return array;
// };

// Alternate solution (without adding second array):
var runningSum = function(nums) {

    // Begin the loop at index 1, since index 0 won't change.
    for (let i = 1; i < nums.length; i++) {

        // Add the sum of the previous index value to the current index.
        nums[i] += nums[i-1];
    }

    return nums;
};


array1 = [1,2,3,4]
array2 = [1,1,1,1,1]
array3 = [3,1,2,10,1]

console.log(runningSum(array1))