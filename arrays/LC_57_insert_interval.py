"""
https://leetcode.com/problems/insert-interval/
"""

class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        """
        *** Note - Intervals are arranged in sorted order, so there's a trick to being efficient here!

        The new interval must either be inserted before, after, or merged with one or more current intervals.

        Since the interval array is pre-sorted, access low to high.

        1) If the new interval goes before the current interval, then add the new interval to the
        return array + all the remaining intervals and return out of the function.

        2) If the new interval goes after the current interval, then add the current interval to the
        return array. The new interval will be inserted at some point in the future, but we don't know where yet!

        3) If the new interval doesn't go before or after, then it must be merged with the current interval.
        Merge the two by taking the lowest and highest values. We don't know if a future interval will also need to be
        merged, so don't add anything to the return array quite yet.

        4) If we've gotten through the list of current intervals and haven't returned out yet, it means the new interval
        was merged with the last interval so we can return out of the function.
        """

        return_array = []

        for i in range(len(intervals)):

            curr_interval = intervals[i]

            # If new interval goes before current interval
            if newInterval[1] < curr_interval[0]:

                # Add new/merged interval, then add rest of current intervals and return out of function
                return_array.append(newInterval)
                return return_array + intervals[i:]     # Adds current + remaining intervals to return array

            # If new interval goes after current interval (future intervals might need to be merged)
            elif newInterval[0] > curr_interval[1]:
                return_array.append(curr_interval)

            # Otherwise, merge new/curr
            else:
                newInterval[0] = min(newInterval[0], curr_interval[0])
                newInterval[1] = max(newInterval[1], curr_interval[1])


        return_array.append(newInterval)
        return return_array


test = Solution()
# intervals = [[1, 3], [6, 9]]
# newInterval = [2, 5]
# # #Expected --> [[1, 5], [6, 9]]

# intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
# newInterval = [4, 8]

# intervals = []
# newInterval = [5, 7]
# #Expected --> [[5, 7]]

# intervals = [[1, 5], [7, 8]]
# newInterval = [4, 6]

# intervals = [[1, 5]]
# newInterval = [5, 7]

# intervals = [[1, 5]]
# newInterval = [6, 8]


output = test.insert(intervals, newInterval)
print(output)
