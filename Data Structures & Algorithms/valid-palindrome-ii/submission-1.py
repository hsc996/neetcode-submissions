class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if it's already a palindrome, return it
        # use slicing to exclude 1 char every iteration, compare as you go
        # if an iteration isn't a match, return false
        if s == s[::-1]:
            return True
        
        for i in range(len(s)):
            new_str = s[:i] + s[i + 1:]
            if new_str == new_str[::-1]:
                return True
        return False