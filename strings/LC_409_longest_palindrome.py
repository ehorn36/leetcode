"""
https://leetcode.com/problems/longest-palindrome/
"""

from collections import defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = defaultdict(int)
        count = 0

        # Store character totals in hashmap
        for char in s:
            hashmap[char] += 1

        # Count the number of pairs
        for value in hashmap.values():

            # If value is even, add to count
            if value % 2 == 0:
                count += value

            # If value is odd, then add the highest even number to count
            else:
                count += value - 1

        # If there's at least 1 character left over (must be an odd straggler, but we can only add 1)
        if count < len(s):
            count += 1

        return count



# s = "abccccdd"
# s = "Aa"
# s = "a"
# s = ""
# s = "abcdf"
s = "bananas"

test = Solution()
print(test.longestPalindrome(s))