class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if openN == closedN == n, return
        # if openN < n, add to openN
        # if closedN < openN, add to closedN
        # recursive solution, using stack
        output = []
        stack = []

        def backtrack(openN, closedN):
            # handle base case
            if openN == closedN == n:
                output.append("".join(stack))
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
        return output