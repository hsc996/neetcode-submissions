class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # init storage -- {key:[]}
        # sort current string, use as key to store unsorted string
        # return values arr to result arr
        store = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            store[sorted_s].append(s)
        return list(store.values())