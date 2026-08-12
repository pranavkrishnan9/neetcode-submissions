class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #input: tokens[] -> array of strings
        #output: int n -> result of the arithmetic operations in tokens in reverse polish notation
        stack = []
        result = 0
        for s in tokens:
            if s == '+' or s == '-' or s == '*' or s == '/':
                b = stack.pop()
                a = stack.pop()
                if s == '+':
                    stack.append(a+b)
                if s == '-':
                    stack.append(a-b)
                if s == '*':
                    stack.append(a*b)
                if s == '/':
                    stack.append(int(a/b))
            else:
                stack.append(int(s))
        return stack[-1]

