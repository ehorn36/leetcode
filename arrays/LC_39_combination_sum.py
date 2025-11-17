"""
https://leetcode.com/problems/combination-sum/
"""

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        *** Description ***
        Given an array of distinct integers candidates and a target integer target,
        return a list of all unique combinations of candidates where the chosen numbers sum to target.
        You may return the combinations in any order.
        The same number may be chosen from candidates an unlimited number of times.
        Two combinations are unique if the frequency of at least one of the chosen numbers is different.
        The test cases are generated such that the number of unique combinations that
        sum up to target is less than 150 combinations for the given input.

        *** Notes ***
        Each num is unique, and can use each num multiple times
        Cannot have duplicates!

        *** Idea / Trick ***
        The idea with this problem is to use a recursive decision tree. Define a new function inside combinationSum()
        which contains two recursive calls: adding the current value, or skipping the current value and then looking at the
        next element. These calls continue until a base case is reached.

        Ordered picking ensures that a previous element is not picked again. Elements are added to each array in
        index order. For example, [2, 2, 3] could be built, but [2, 3, 2] (which is a duplicate / permutation) is
        impossible. This is because once number 2 is moved-on from, it will never be seen again. Furthermore, every

        Base case #1: sum of values = target ==> add combination to answer array & return nothing
        Base case #2: Sum of values > target ==> return nothing
        Base case #3: Sum of values < target + ran out of elements == return nothing

        Add value ==> call recursive_function() and add the current element to the array.

        Add value ==> call recursive_function() and don't add the current element. Increase the index of i to point to
        the next element

        """

        answer_array = []

        def recursive_decision_tree(i: int, current_sum: int, current_array: list):

            # Base case #1: Target found
            if current_sum == target:
                answer_array.append(current_array)
                return

            # Base case #2: CombinationSum is too large
            elif current_sum > target:
                return

            # Base case #3: No more elements to consider
            elif i > len(candidates) - 1:
                return

            else:

                # Add element to combinationSum and update array. Keep index the same
                new_sum = current_sum + candidates[i]
                updated_array = current_array + [candidates[i]]     # Note - can't use .append() because it returns None
                recursive_decision_tree(i, new_sum, updated_array)

                # Don't add element to sum or list, increment index
                recursive_decision_tree(i + 1, current_sum, current_array)

        recursive_decision_tree(0, 0, [])
        return answer_array


candidates = [2, 3, 6, 7]
target = 7
Output: [[2,2,3],[7]]

# candidates = [2,3,5]
# target = 8
# # Output: [[2,2,2,2],[2,3,3],[3,5]]

# candidates = [2]
# target = 1
# # Output: []

test = Solution()
print(test.combinationSum(candidates, target))
