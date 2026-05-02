class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = set(nums)

        if len(hash) == len(nums):
            return False
        
        return True