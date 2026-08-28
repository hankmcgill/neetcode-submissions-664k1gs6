class Solution:
    def isValid(self, s: str) -> bool:
        PAIRS = {'(':')','{':'}','[':']'}
        stack = []
            
        for char in s:
            if len(stack) == 0 and char in PAIRS.values():
                    return False
            if char in PAIRS.keys():
                stack.append(char)
            elif PAIRS[stack[-1]] == char:
                stack.pop()

        return (len(stack) == 0)