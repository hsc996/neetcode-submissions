class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pairs: temp, index

        for i, t in enumerate(temperatures):
            # While stack is not empty and temp is greater than v on top of stack
            while stack and t > stack[-1][0]:
                # Pop from top of stack
                stackT, stackInd = stack.pop()
                # Calculate difference between indexes (days since hottest temp)
                res[stackInd] = (i - stackInd)
            # Append new hottest temp and its index
            stack.append([t, i])
        return res