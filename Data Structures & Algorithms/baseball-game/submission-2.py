class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        stack = []

        # add each event to the stack
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else: # handle regular scores
                stack.append(int(op))

        # then pop everything off stack
        while stack:
            val = stack.pop()
            score += val

        return score