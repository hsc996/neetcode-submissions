class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        count = 1
        maxf = 0

        for i in range(len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
                i += 1
            else:
                count = 1
            maxf = max(maxf, count)
        return maxf