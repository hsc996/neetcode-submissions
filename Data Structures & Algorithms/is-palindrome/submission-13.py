class Solution:
    def isPalindrome(self, s: str) -> bool:
        n_str = ""
        for c in s:
            if c.isalnum():
                n_str += c.lower()
        return n_str == n_str[::-1]