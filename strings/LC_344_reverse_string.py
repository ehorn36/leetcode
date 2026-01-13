"""
https://leetcode.com/problems/reverse-string/description/

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

    Example 1:
        Input: s = ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]

    Example 2:
        Input: s = ["H","a","n","n","a","h"]
        Output: ["h","a","n","n","a","H"]
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s) - 1

        while left < right:
            # Swap places
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            # Move pointers
            left += 1
            right -= 1

        return s


# s = ["h", "e", "l", "l", "o"]
# s = ["h"]
s = ["h", "a", "n", "d"]
test = Solution()
print(test.reverseString(s))
