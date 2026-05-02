class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filter string to alnum and ensure lowercase
        # reverse string and cross reference - return boolean
        result = ""

        for c in s:
            if c.isalnum():
                result += c.lower()
        return result == result[::-1]