class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # can use recursive solution + stack
        # rules:
        # if openC < n, add open par
        # if closedC < openC, add closed par
        # if openC == closedC == n, complete/add to result
        stack = []
        res = []

        def backtrack(openC, closedC):
            # handle base case
            if openC == closedC == n:
                res.append("".join(stack))
                return
            
            if openC < n:
                stack.append("(")
                backtrack(openC + 1, closedC)
                stack.pop()
            
            if closedC < openC:
                stack.append(")")
                backtrack(openC, closedC + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res