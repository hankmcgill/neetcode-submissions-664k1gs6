class Solution:
    def isValid(self, s: str) -> bool:
        PAIRS = {'(':')','{':'}','[':']'}
        stack = []
            
        for char in s:
            if char in PAIRS.keys():
                stack.append(char)
            elif PAIRS[stack[-1]] == char:
                stack.pop()
            else:
                return False

        return (len(stack) == 0)