"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        # Note - if an array is sorted or must be accessed in a certain manner (forward in time),
        then there's probably a 'trick' or efficient way of creating the algorithm.

        Example:
        prices[7, 2, 4, 5, 1, 3, 6, 4]

        *** Easy way is to brute force in O(n^2), but this is inefficient. Can be achieved in O(n) time.

        The key to this problem is that time moves in 1 direction, starting on the first day ('trick').
        As you move left to right, if the current price results in a loss ($7 --> $2), then the sell price must be lower
        than the buy price, and moving forward will be the best possible price to buy at!
        Thus, you should update your buy price to the current sell price ($2, which is lower).

        If the next current price results in a profit ($2 --> $4), great! Compare your current profit to the max profit,
        and take the larger number. Then, check the next price.

        Do this until you've looked at all the prices.
        """

        # Pointers
        buy = 0     # Start on day 1
        sell = 1    # Start on day 2

        max_profit = 0
        while sell < len(prices):   # Must use while loop since sell starts at index 1.
                                    # For loop would result in sell index being at len + 1, which is out of range
            # If profit
            if prices[buy] < prices[sell]:

                current_profit = (prices[sell] - prices[buy])
                max_profit = max(max_profit, current_profit)

            # If loss (sell lower than buy)
            else:
                buy = sell          # Sell is lower than buy, so that's the new low price

            # Then, check the next price
            sell += 1

        return max_profit



test = Solution()

prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]

output = test.maxProfit(prices)
print(output)
