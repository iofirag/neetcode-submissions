class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        pairs = {'(':')', '{':'}', '[':']'}
        stack = []

        for c in s:
            if c in pairs.keys():
                stack.append(c)
            elif c in pairs.values():
                if not stack:
                    return False
                if pairs[stack.pop()] != c:
                    return False
            else:
                return False
                
        return len(stack) == 0
