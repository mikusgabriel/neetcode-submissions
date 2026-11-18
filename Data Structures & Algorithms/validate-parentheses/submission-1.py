class Solution:
    def isValid(self, s: str) -> bool:

        info = {'{': '}', '(' : ')', '[': ']'}
        stack = []
        for i in range(0,len(s)):
            char = s[i]
            if len(stack) == 0:
                stack.append(char)
                continue
            top = stack[-1]
            
            if top in info and char == info[top]:
                stack.pop(-1)
            else:
                stack.append(char)



        if len(stack) == 0:
            return True

        return False