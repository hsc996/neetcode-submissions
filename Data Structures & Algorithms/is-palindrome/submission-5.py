class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filter string to ensure all chars are alnum
        # reverse string
        # return boolean
        sorted = ""

        for char in s:
            if char.isalnum():
                sorted += char.lower()
        
        return sorted == sorted[::-1]
