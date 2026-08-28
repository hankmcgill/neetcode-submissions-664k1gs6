class Solution:
    def isValid(self, s: str) -> bool:
        PAIRS = {'(':')','{':'}','[':']'}
        stack = []

        for char in s:
            if char in PAIRS.keys():
                stack.append(char)
            elif not stack:
                return False
            elif stack and char in PAIRS.values() and PAIRS[stack[-1]] == char:
                stack.pop()

        return (len(stack) == 0)