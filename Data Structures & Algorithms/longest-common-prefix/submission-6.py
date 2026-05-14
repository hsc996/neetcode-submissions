class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #store first word as prefix
        #iterate though list of strings
            #iterate through chars -- while j < min length prefix + current string
            # if the chars don't match, break loop
        # iterate j
        # update prefix var with new longest
        prefix = strs[0]

        for i in range(len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix
