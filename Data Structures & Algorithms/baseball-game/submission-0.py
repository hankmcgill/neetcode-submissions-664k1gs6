class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        prev_1 = 0
        prev_2 = 0
        for operation in operations:
            if operation == '+':
                score += (prev_1 + prev_2)
            elif operation == 'D':
                if not prev_2:
                    score += (2 * prev_1)
                else:
                    score += (2 * prev_2)
            elif operation == 'C':
                if prev_2:
                    score -= (prev_2 + prev_1)
                    prev_2 = 0
                else:
                    score -= prev_1
                    prev_1 = 0
            else:
                score += int(operation)
                if not prev_1:
                    prev_1 = int(operation)
                else:
                    prev_2 = int(operation)
            print(score)

        return score