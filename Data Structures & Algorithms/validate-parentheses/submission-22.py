class Solution:
    def isValid(self, s: str) -> bool:
        PAIRS = {'(':')','{':'}','[':']'}
        stack = []

        if len(s) < 2:
            return False

        for char in s:
            if stack and stack[-1] in PAIRS.keys():
                if PAIRS[stack[-1]] == char:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return (len(stack) == 0)