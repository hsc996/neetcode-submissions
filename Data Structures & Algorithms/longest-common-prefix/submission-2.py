class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # scan horizontally
        # save first word as prefix
        # iterate through element, comparing with prefix (but shrink search to only common portion)
        # if they no longer match, break the loop
        # truncate prefix to include only chars from 0-j+1
        prefix = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix