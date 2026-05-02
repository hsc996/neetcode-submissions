class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # use first string as prefix
        # compare each element of prefix with each string in str_arr
        # break loop when elements stop matching
        # reset prefix to prefix up to j element
        prefix = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix