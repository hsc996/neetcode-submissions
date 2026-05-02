class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1: count with hashmap
        # step 2: sort, where c = i
        # step 3: iterate backwards through freq
        # step 4: as soon as k elements found, return them
        count = {} #{n:c}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res