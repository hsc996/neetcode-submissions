class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use a dict to store in groups -> using sorted version as key
        store = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            store[sorted_s].append(s)
        return list(store.values())