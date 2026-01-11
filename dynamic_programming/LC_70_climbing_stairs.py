"""
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

class Solution(object):
    def climbStairs(self, n):
        """
        Bottom up tabulation, constant space
        Time: O(n)
        Space: O(1)
        """

        # If n is 1 or 2, return n
        if n <= 2:
            return n

        # Set pointers
        prev = 1
        curr = 2
        for _ in range(2, n):   # Goes from 2 --> (n - 1)

            # Determine next value
            next_val = prev + curr

            # Update pointers
            prev = curr
            curr = next_val


        return curr

    def climbStairs2(self, n):
        """
        Bottom up tabulation
        Time: O(n)
        Space: O(n)
        """

        # Create storage array with placeholder values
        dp = 0 * n
        dp[0] = 1   # 1 way for 1 step
        dp[1] = 2   # 2 ways for 2 steps, etc.

        # Iterate through indexes 2 -> (n - 1)
        for i in range(2, n):

            # Current element == sum of previous two elements
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n - 1]

    def climbStairs3(self, n):
        """
        Memoization solution
        Time: O(n)
        Space: O(n)
        """

        memo = {}   # Hashtable

        def f(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = f(n-2) + f(n-1)
                return memo[n]

        return f(n)

    def climbStairs4(self, n):
        """
        Recursive solution
        Time: O(2^n)
        Space: O(n)
        """

        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs4(n - 2) + self.climbStairs4(n - 1)








test = Solution()
print(test.climbStairs(5))