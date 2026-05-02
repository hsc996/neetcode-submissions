class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # handle edge case - if array is empty (as rest of code assumes there is at lease 1 value)
        if not nums:
            return 0
        
        # sort and remove duplicates
        sorted_set = sorted(set(nums))
        curr_count = 1 # as we are starting from second element when iterating
        max_seq = 0

        for i in range(len(sorted_set)):
            if sorted_set[i] == sorted_set[i - 1] + 1:
                curr_count += 1
            else:
                curr_count = 1 # reset count
            max_seq = max(max_seq, curr_count)
        return max_seq