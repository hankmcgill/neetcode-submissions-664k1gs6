class Solution:
    def isValid(self, s: str) -> bool:
        PAIRS = {'(':')','{':'}','[':']'}
        stack = []

        if len(s) < 2:
            return False

        for char in s:
            if char in PAIRS.keys():
                stack.append(char)
            elif PAIRS[stack[-1]] == char:
                stack.pop()

        return (len(stack) == 0)