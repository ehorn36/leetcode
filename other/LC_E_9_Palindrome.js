const isPalindrome = function(x) {
    let string1 = x.toString();
    let string2 = ""
     
    // (i = string.length - 1) because we're starting at the last index of string and moving backwards.
    for (let i = string1.length - 1; i >= 0; i--) {
        string2 += string1[i];
    }

    if (string1 === string2) {
        return true;
    } 
    
    else {
        return false;
    }
};

console.log(isPalindrome(121));