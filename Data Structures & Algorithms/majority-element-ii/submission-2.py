class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold  = len(nums) // 3
        count = {}
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            if c > threshold:
                res.append(n)
        return res