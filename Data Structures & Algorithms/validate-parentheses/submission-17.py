class Solution:
    def isValid(self, s: str) -> bool:
        PAIRS = {'(':')','{':'}','[':']'}
        stack = []

        for char in s:
            if char in PAIRS.keys():
                stack.append(char)
            elif PAIRS[stack[-1]] != char:
                return False
            else:
                stack.pop()

        return (len(stack) == 0)