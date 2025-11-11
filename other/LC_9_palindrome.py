class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_1 = str(x)               # Convert int to string.
        string_2 = string_1[::-1]       # Assign reversed version of string.

        if string_1 == string_2:
            return True
        else: 
            return False

map = Solution().isPalindrome(4)
print(map)