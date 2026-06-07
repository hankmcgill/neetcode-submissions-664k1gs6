class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largest = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            if (r, c) in visited:
                return 0
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0

            visited.add((r, c))

            return (1 + bfs(r + 1, c) +
            bfs(r - 1, c) +
            bfs(r, c + 1) +
            bfs(r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited:
                    largest = max(largest, bfs(r, c))

        return largest