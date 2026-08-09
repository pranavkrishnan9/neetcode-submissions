class Solution:
    def isValid(self, s: str) -> bool:
        #not stack = checks if the stack is empty -> returns true if empty, false if not
        #stack.pop() = removes and returns the element at the top of the stack
        #stack[-1] = allows you to peek at the element at the top of the stack
        #stack.append() = allows you to append an element to the top of the stack
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack or pairs[stack[-1]] != c:
                    return False
                stack.pop()
        return not stack
            
            