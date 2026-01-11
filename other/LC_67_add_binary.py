"""
https://leetcode.com/problems/add-binary/description/

Given two binary strings a and b, return their sum as a binary string.

    Example 1:
        Input: a = "11", b = "1"
        Output: "100"

    Example 2:
        Input: a = "1010", b = "1011"
        Output: "10101"

Note:
    * Reverse strings a, b
    * Traverse longest string
    * Add a + b + carry bit
    * If beyond index of string, use 0
    * Make sure to add the last carry bit
"""

class Solution(object):
    def addBinary(self, a, b):

        carry = 0
        return_string = ""

        # Reverse input strings, (aka create a slice from beg <-- end, going backwards)
        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):

            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0

            total = digit_a + digit_b + carry
            if total == 0:
                return_string = "0" + return_string
                carry = 0
            elif total == 1:
                return_string = "1" + return_string
                carry = 0
            elif total == 2:
                return_string = "0" + return_string
                carry = 1
            elif total == 3:
                return_string = "1" + return_string
                carry = 1

        if carry > 0:
            return_string = "1" + return_string

        return return_string

test = Solution()
print(test.addBinary("11", "1"))