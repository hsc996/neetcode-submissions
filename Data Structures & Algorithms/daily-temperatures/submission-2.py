class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        While temp hotter than top of stack,
        Pop element and index from stack,
        Calculate difference in indices of current temp and stack,
        Append new temp + index to stack,
        Return
        '''
        res = [0] * len(temperatures)
        stack = [] # pairs: temp, index (days since)

        for i, t in enumerate(temperatures):
            # while stack is non-empty and temp is greater than v @ top of stack
            while stack and t > stack[-1][0]:
                # Pop element at the top of the stack
                stackT, stackInd = stack.pop()
                # Calculate difference between indicies (days since last hottest temp)
                res[stackInd] = (i - stackInd)
                # Append new hottest temp and its index to stack
            stack.append([t, i])
        return res