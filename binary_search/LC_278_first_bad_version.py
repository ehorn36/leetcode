"""
https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad
version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad. You are given an API bool isBadVersion(version)
which returns whether version is bad. Implement a function to find the first bad version.
You should minimize the number of calls to the API.

    Example 1:
        Input: n = 5, bad = 4
        Output: 4
        Explanation:
        call isBadVersion(3) -> false
        call isBadVersion(5) -> true
        call isBadVersion(4) -> true
        Then 4 is the first bad version.

    Example 2:
        Input: n = 1, bad = 1
        Output: 1

Note
 * This is just searching for N among a list of versions - AKA binary search.
 * N is an int and is 1-indexed, it's not a list.
 * Since we're looking for the first bad version, not a particular number, the algo is slightly different than
   binary search. When mid == bad, that's the lowest found bad. Rather than set the R pointer to mid - 1, we set to
   mid and return that value as the first bad.
"""

def isBadVersion(n):
    if n >= 1:
        return True
    else:
        return False

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # Set pointers, the first possible bad version is 1, the last is n
        left = 1
        right = n

        while left < right:

            mid = (left + right) // 2

            # If mid is bad, it's the lowest identified bad version
            if isBadVersion(mid):
                right = mid

            # Mid must be good
            else:
                left = mid + 1

        return right

test = Solution()
print(test.firstBadVersion(1))







