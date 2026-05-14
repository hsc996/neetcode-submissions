class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use dict to store list of options -> key will be storted version of string
        result = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            result[sorted_s].append(s)
        return list(result.values())