"""
https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input
        string is valid. An input string is valid if:

        * Open brackets must be closed by the same type of brackets.
        * Open brackets must be closed in the correct order.
        * Every close bracket has a corresponding open bracket of the same type.

        Example 1:
            Input: s = "()"
            Output: true

        Example 2:
            Input: s = "()[]{}"
            Output: true

        Example 3:
            Input: s = "(]"
            Output: false

        Example 4:
            Input: s = "([])"
            Output: true

        Example 5:
            Input: s = "([)]"
            Output: false

        Constraints:

            1 <= s.length <= 104                        (can have 1 to 104 items in the string)
            s consists of parentheses only '()[]{}'.    (Only 3 different characters can be allowed)

        *** Eric's Notes ***
        This problem is about matching bracket pairs is the correct order, where the most recent open parentheses needs
        to be closed first. This is a last-in-first-out situation, which is exactly how a stack operates.

        The idea is to loop through the string once. As you travel the string, add open brackets the top of the stack.
        If you encounter a closed bracket, if the open bracket at the stop of the stack is of the same type, pop the
        open bracket off the stack and continue parsing the string. If it's not the same type, return False. If you
        get to the end of the string and the stack is empty, then all brackets are valid and return True.
        """

        # Create stack
        stack = []

        # Key = closed bracket, Value = corresponding open bracket
        hashmap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # Traverse string
        for parentheses in s:

            # If parentheses found in hashmap (it's a closed bracket)
            if parentheses in hashmap:

                # If the stack is not empty, and the open bracket at the top of the stack is the correct type
                if stack and (stack[-1] == hashmap[parentheses]):

                    # Pop the open parentheses off the top of the stack
                    stack.pop()     # .pop() == remove last item from array. Stack adds to back of array

                # Parentheses don't match, or stack is empty (can't begin pair with closed bracket)
                else:
                    return False

            # Else, parentheses not found in hashmap (it's an open bracket)
            else:
                stack.append(parentheses)   # .append() == add item to back of array. Stack adds to back of array

        # If stack is empty, return True. Otherwise, return False.
        return not stack


# s = "([)]"        # False
# s = "()[]{}"      # True
# s = "(]"          # False
# s = "([])"        # True
s = "({[]}){[]}"   # True

test = Solution()
print(test.isValid(s))


