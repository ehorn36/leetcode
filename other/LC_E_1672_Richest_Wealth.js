const maximumWealth = function(accounts) {
    largest = 0;
    for (i = 0; i < accounts.length; i++) {
        localSum = 0;
        for (j = 0; j < accounts[i].length; j++) {
            localSum += accounts[i][j];
        }
        if (localSum > largest) {
            largest = localSum;
        }
    }
    return largest;
};

array1 = [[1,2,3],[3,2,1]]
array2 = [[1,5],[7,3],[3,5]]
array3 = [[2,8,7],[7,1,3],[1,9,5]]

console.log(maximumWealth(array3));

// In Javascript, ".length" is a property, not a method. Therefore, calling .length doesn't require trailing parathesis (i.e. .length()) as in other langauges. 