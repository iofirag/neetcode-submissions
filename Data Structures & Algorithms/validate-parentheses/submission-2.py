class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        charmap = {
            '(':')', 
            '{':'}', 
            '[':']'
        }
        stack = []

        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
            elif c in ['}',']',')']:
                if len(stack) == 0:
                    return False
                openc = stack.pop()
                if charmap[openc] != c:
                    return False
            else:
                return False
                
        return len(stack) == 0
