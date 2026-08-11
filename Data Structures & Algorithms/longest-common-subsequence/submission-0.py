class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_grid = [[0 for j in range(len(text2) + 1)] 
                   for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp_grid[i][j] = 1 + dp_grid[i + 1][j + 1]
                else:
                    dp_grid[i][j] = max(
                        dp_grid[i + 1][j],
                        dp_grid[i][j + 1]
                    )

        return dp_grid[0][0]