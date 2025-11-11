class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return
        an array of the non-overlapping intervals that cover all the intervals in the input.

        Example 1:

            Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
            Output: [[1,6],[8,10],[15,18]]
            Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

        Example 2:

            Input: intervals = [[1,4],[4,5]]
            Output: [[1,5]]
            Explanation: Intervals [1,4] and [4,5] are considered overlapping.

        Constraints:

            1 <= intervals.length <= 10^4    (number of intervals in the input list -> at least 1)
            intervals[i].length == 2        (length of each interval within the list = 2 elements)
            0 <= starti <= endi <= 10^4      (start/end value could be from 0 -> 10^4

        Eric's notes:

            Notice the input array isn't sorted, meaning you could have [[1, 4], [0, 0]]
        """

        # sort by key, where 'key' = output of called function (lambda == nameless function)
        # lamda (current interval): output = (current interval --> index 0)
        intervals.sort(key=lambda i: i[0])
        answer_array = []

        # Iterate over intervals (at least 1 interval in list)
        pending_interval = []
        for interval in intervals:

            # If pending empty, then add curr interval to pending
            if len(pending_interval) == 0:
                pending_interval = interval

            # elif curr min <= pending max (need to merge)
            elif interval[0] <= pending_interval[1]:
                pending_interval[0] = min(interval[0], pending_interval[0])
                pending_interval[1] = max(interval[1], pending_interval[1])

            # elif curr min > pending max (add pending)
            elif interval[0] > pending_interval[1]:
                answer_array.append(pending_interval)
                pending_interval = interval

        answer_array.append(pending_interval)
        return answer_array


# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]     # Output: [[1, 6], [8, 10], [15, 8]]
intervals = [[1, 4], [4, 5]]                        # [[1, 5]]
# intervals = [[0, 1], [5, 6]]                        # [[0, 1], [5, 6]]
# intervals = [[1,4],[0,0]]                           # [[0,0],[1,4]]

test = Solution()
print(test.merge(intervals))
