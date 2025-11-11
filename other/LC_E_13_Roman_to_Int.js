var romanToInt = function(s) {
    const array = {I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000};
    let int = 0;

    // Loop through Roman numeral string. Must use "let", since i++ wont work using "const."
    for (let i = 0; i < s.length; i++) {

        // Account for Roman numeral subtraction: IX == 4, or IV == 9.
        if (i < s.length - 1 && s[i] === 'I') {
            if (s[i+1] === 'V') {
                int += 4;
                i++;
                continue;
            }      
            else if (s[i+1] === 'X') {
                int += 9;
                i++;
                continue;
            }
        }
        // Account for Roman numeral subtraction: XL == 40, or XC == 90.
        else if (i < s.length - 1 && s[i] === 'X') {
            if (s[i+1] === 'L') {
                int += 40;
                i++;
                continue;
            }      
            else if (s[i+1] === 'C') {
                int += 90;
                i++;
                continue;
            } 
        }
        // Account for Roman numeral subtraction: CD == 400, or CM == 900.
        else if (i < s.length - 1 && s[i] === 'C') {
            if (s[i+1] === 'D') {
                int += 400;
                i++;
                continue;
            }      
            else if (s[i+1] === 'M') {
                int += 900;
                i++;
                continue;
            }
        }
        // For everything else.
        for (const [key, value] of Object.entries(array)) {

            // If string character == array key, then add array value to int.
            if (s[i] === key) {
                int += parseInt(value);
                break;
            }
        }

    }
    return int;
};

let input = romanToInt("MCMXCIV");
console.log(input);