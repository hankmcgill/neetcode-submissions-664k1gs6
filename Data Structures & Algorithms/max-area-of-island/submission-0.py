class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largest = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            # water or already visited
            if grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))

            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    curr_size = dfs(r, c)
                    largest = max(largest, curr_size)

        return largest