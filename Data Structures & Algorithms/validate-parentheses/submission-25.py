class Solution:
    def isValid(self, s: str) -> bool:
        PAIRS = {'(':')','{':'}','[':']'}
        stack = []

        for char in s:
            if stack and stack[-1] in PAIRS.keys():
                if PAIRS[stack[-1]] == char:
                    stack.pop()
                    continue
            stack.append(char)

        return (len(stack) == 0)