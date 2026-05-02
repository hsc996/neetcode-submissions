class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                # Will convert to an int and round it towards zero at the same time
                stack.append(int(b / a))
            else:
                # Covert to a number before returning it as we was to return a number
                stack.append(int(c))

        return stack[0]