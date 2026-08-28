class Solution:
    def isValid(self, s: str) -> bool:
        PAIRS = {'(':')','{':'}','[':']'}
        stack = []
            
        for char in s:
            if char in PAIRS.keys():
                stack.append(char)
            elif PAIRS[stack[-1]] == char:
                if len(stack) == 0:
                    return False
                stack.pop()

        return (len(stack) == 0)