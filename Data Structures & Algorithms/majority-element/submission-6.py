class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashmap to store number + count
        # max_c to store current max count
        # if current count > max_c, update as we go + update res
        count = defaultdict(int)
        res = 0
        max_c = 0

        for n in nums:
            count[n] += 1
            if max_c < count[n]:
                max_c = count[n]
                res = n
        return res