class Solution:
    def isPalindrome(self, s: str) -> bool:
        # case sensitive - convert to one case
        # alnum only
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]