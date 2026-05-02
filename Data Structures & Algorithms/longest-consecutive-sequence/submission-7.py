class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums = sorted(set(nums))
        max_c = 0
        curr_count = 1

        for i in range(len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr_count += 1
            else:
                curr_count = 1
            max_c = max(max_c, curr_count)
        return max_c