class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #initial stack

        close = {")": "(", "]": "[", "}": "{"} #Open to close

        # The idea is to create a stack to store the inputs 
        # for each char c in the string 
        #      if the bracket is opening push it onto the stack 
        #      if it is closing 
        # check if the stack is empty and its top matches the corresponding bracket
        # if yes pop the stack
        # or return false
        for c in s:
            if c in close:
                if stack and stack[-1] == close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        