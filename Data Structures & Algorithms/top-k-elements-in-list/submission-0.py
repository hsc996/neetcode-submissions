from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted = counter.most_common()
        st = []
        for i in range(k):
            st.append(sorted[i][0])
        return st
