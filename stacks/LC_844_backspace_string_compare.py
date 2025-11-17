"""
https://leetcode.com/problems/backspace-string-compare/
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a
        backspace character. Note that after backspacing an empty text, the text will continue empty.

        Example 1:

            Input: s = "ab#c", t = "ad#c"
            Output: true
            Explanation: Both s and t become "ac".

        Example 2:

            Input: s = "ab##", t = "c#d#"
            Output: true
            Explanation: Both s and t become "".

        Example 3:

            Input: s = "a#c", t = "b"
            Output: false
            Explanation: s becomes "c" while t becomes "b".
        """

        # *** Stack solution ***
        # stack1 = []
        # for i in range(len(s)):
        #
        #     # If character is a "#" and the stack isn't empty, remove the previous element
        #     if s[i] == "#" and len(stack1) != 0:
        #         stack1.pop()
        #
        #     # Otherwise, add alphabetic characters to stack
        #     else:
        #         if s[i] != "#":
        #             stack1.append(s[i])
        #
        # # Do the same thing for the second string
        # stack2 = []
        # for j in range(len(t)):
        #     if t[j] == "#" and len(stack2) != 0:
        #         stack2.pop()
        #     else:
        #         if t[j] != "#":
        #             stack2.append(t[j])
        #
        # # Compare strings
        # return stack1 == stack2

        # *** Non-stack solution ***
        index_s = len(s) - 1
        index_t = len(t) - 1

        while index_t >= 0 or index_s >= 0:

            # Find the next valid character
            index_s = next_valid_char(s, index_s)
            index_t = next_valid_char(t, index_t)

            # Assign to char or empty string if index out of bounds
            char_s = s[index_s] if index_s >= 0 else ""
            char_t = t[index_t] if index_t >= 0 else ""

            # if the chars don't match, return False
            if char_s != char_t:
                return False

            index_s -= 1
            index_t -= 1

        # If we haven't returned False, then must be True
        return True

def next_valid_char(string, index) -> int:

    backspaces = 0
    while index >= 0:

        # If valid character found and no backspaces left, break out of loop
        if backspaces == 0 and string[index] != "#":
            break

        # If backspace character found
        elif string[index] == "#":
            backspaces += 1

        # If valid character found, but there are backspaces left to process
        else:
            backspaces -= 1

        # Then, look at the next index
        index -= 1

    # Return current index
    return index



# s, t = "ab#c", "ad#c"       # True
# s, t = "ab##", "c#d#"       # True
# s, t = "a#c", "b"           # False
# s, t = "a##c", "#a#c"       # True
# s, t = "y#fo##f", "y#f#o##f"    # True
s, t = "xywrrmp", "xywrrm#p"   # False


test = Solution()
print(test.backspaceCompare(s, t))