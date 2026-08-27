class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        stack = []

        # add each event to the stack
        for op in operations:
            if op == '+':
                stack.append((('sum'), stack[-1][1] + stack[-2][1]))
            elif op == "D":
                stack.append((('double'), stack[-1][1] * 2))
            elif op == "C":
                stack.pop()
            else: # handle regular scores
                stack.append(('score', int(op)))

        # then pop everything off stack
        while stack:
            last_event = stack.pop()
            desc, val = last_event
            score += val

        return score