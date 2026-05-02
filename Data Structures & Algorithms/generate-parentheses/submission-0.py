class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open par if open < n
        # only add closed par if closed < open
        # only valid IF open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            # handle base case
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res