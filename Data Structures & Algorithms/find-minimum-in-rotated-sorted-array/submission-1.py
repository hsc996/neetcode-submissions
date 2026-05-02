class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            m = lo + (hi - lo) // 2
            if nums[m] < nums[hi]:
                hi = m
            else:
                lo = m + 1
        return nums[lo]
