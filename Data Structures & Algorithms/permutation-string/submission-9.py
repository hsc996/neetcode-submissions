class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sort s1 for reference point
        # loop through difference n1 and n2
        # set j pointer n1 spaces away
        #slice i:j, sort and compare to s1
        n1, n2 = len(s1), len(s2)
        s1 = sorted(s1)

        for i in range(n2-n1 + 1):
            j = i + n1
            substr = s2[i:j]
            substr = sorted(substr)
            if substr == s1:
                return True
        return False