class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        s1 = sorted(s1)

        for i in range(n2 - n1 + 1):
            j = i + n1
            substr = s2[i:j]
            substr = sorted(substr)
            if substr == s1:
                return True
        return False