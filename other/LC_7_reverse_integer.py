"""
https://leetcode.com/problems/reverse-integer/description/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0. Assume the environment does not allow you to store
64-bit integers (signed or unsigned).

    Example 1:
        Input: x = 123
        Output: 321

    Example 2:
        Input: x = -123
        Output: -321

    Example 3:
        Input: x = 120
        Output: 21

Just reverse the digits using modulo 10 & dividing the remaining value by 10. If the value is outside the signed
integer range, then return 0.

"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        INT_MAX = (2 ** 31) - 1

        # If x < 0 = True, then is_neg == True
        is_neg = x < 0

        # Ensure integer x is positive
        x = abs(x)

        result = 0

        # While x > 0
        while x:

            # Determine 1's place
            digit = x % 10      # (ex. 15 / 10 = 1.5, r = 5)
            x //= 10            # Remove digit from X

            # If res result is too big
            if result > (INT_MAX - digit) // 10:
                return 0

            # Add digit to result
            result = (result * 10) + digit

        return -result if is_neg else result
