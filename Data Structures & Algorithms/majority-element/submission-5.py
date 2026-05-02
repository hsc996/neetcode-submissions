class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # init hashmap to store count
        #init max_c & res
        # iterate through nums:
            # add current number to count
            # if count of current value > max_c:
                #set as new max_c
                # update res to this number
        count = defaultdict(int)
        max_c = 0
        res = 0

        for n in nums:
            count[n] += 1
            if max_c < count[n]:
                max_c = count[n]
                res = n
        return res