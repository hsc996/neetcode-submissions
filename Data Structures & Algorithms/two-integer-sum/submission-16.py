class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # track value, index in hashmap
        # find complement of target + current value
        # if complement in hashmap, return index of value + current index
        # otherwise add to hashmap
        seen = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i