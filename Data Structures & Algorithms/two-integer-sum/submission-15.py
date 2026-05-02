class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store {value:index} pairs in hashmap
        # find the complement: target - current value
        # check hashmap for complement
            #if found
                # return indexes of complement & current value
            # else
                # add current value & index to hashmap
        #if no pair found, return -1
        hashmap = {}

        for i, n in enumerate(nums):
            tmp = target - n
            if tmp in hashmap:
                return [hashmap[tmp], i]
            hashmap[n] = i
        return -1