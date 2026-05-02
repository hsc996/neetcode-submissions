class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # store first work as prefix
        # iterate through the list
        # init j pointer for element iteration
        # while j < min common portion, loop through
        # if no match, break
        # move j for left slice to update prefix to current longest
        prefix = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix