class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        longest_common_prefix = ""

        # Traverse characters in first / reference string
        for i in range(len(strs[0])):

            # Traverse all strings in array
            for string in strs:

                # If i == the length of the current string, then it's out of bounds.
                # Or, if the characters don't match
                if i == len(string) or string[i] != strs[0][i]:

                    # Return the longest existing prefix
                    return longest_common_prefix

            # Otherwise, add the current character to the longest prefix (once you've gone through all the strings)
            longest_common_prefix += strs[0][i]

        return longest_common_prefix

strs = ["flower", "flow", "flight"]
# strs = ["dog", "racecar", "car"]

test = Solution()
print(test.longestCommonPrefix(strs))
