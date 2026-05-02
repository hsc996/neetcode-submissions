class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for k, v in count.items():
            if v > (len(nums) / 3):
                res.append(k)
        
        return res