class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        prev_row = [0] * cols

        for r in range(rows - 1, -1, -1):
            curr_row = [0] * cols

            for c in range(cols - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curr_row[c] = 0
                elif r == rows - 1 and c == cols - 1:
                    curr_row[c] = 1
                else:
                    right = curr_row[c + 1] if c + 1 < cols else 0
                    down = prev_row[c]
                    curr_row[c] = right + down

            prev_row = curr_row

        return prev_row[0]