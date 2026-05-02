class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        While current temp hotter than top of stack,
        Pop element and index from stack,
        Calculate difference in indices of current temp and stack,
        Append new temp + index to stack,
        Return
        '''
        res = [0] * (len(temperatures))
        stack = [] # [t, i]

        for i, t in enumerate(temperatures):
            # while stack not empty + current temp > temp @ top of stack
            while stack and t > stack[-1][0]:
                # pop pair at top of stack
                stack_t, stack_i = stack.pop()
                # calculate difference in indices (days since)
                res[stack_i] = (i - stack_i)
            # append new hottest temp to stack
            stack.append([t, i])
        return res

