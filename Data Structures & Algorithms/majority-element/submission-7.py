class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return NUMBER, not count itself
        # dict to store count {n:c}
        # update max count + current maj as you go
        count = defaultdict(int)
        res = 0
        maxc = 0 

        for n in nums:
            count[n] += 1
            if maxc < count[n]:
                maxc = count[n]
                res = n
        return res