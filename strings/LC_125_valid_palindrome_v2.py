class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        alpha_only_forwards = []
        alpha_only_backwards = []

        for char in s:
            if char.isalnum():
                alpha_only_forwards.append(char.upper())

        for char in s[::-1]:
            if char.isalnum():
                alpha_only_backwards.append(char.upper())

        if alpha_only_forwards == alpha_only_backwards:
            return True
        return False


# s = "A man, a plan, a canal: Panama"        # True
# s = "race a car"                            # False
# s = " "                                     # True
# s = "0P"                                    # False

test = Solution()
print(test.isPalindrome(s))

