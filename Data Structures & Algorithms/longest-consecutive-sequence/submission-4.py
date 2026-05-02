class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #if not arr, return -1
        # sort + set arr
        # curr_max  + max count
        # check if n = n-1, if so - add to curr max
        # find max count
        if not nums:
            return 0
        
        sorted_nums = sorted(set(nums))
        curr_max = 1
        max_count = 0

        for i in range(len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                curr_max += 1
            else:
                curr_max = 1
            
            max_count = max(max_count, curr_max)

        return max_count