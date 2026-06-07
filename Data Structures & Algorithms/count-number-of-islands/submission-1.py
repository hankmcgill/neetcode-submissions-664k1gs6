class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # base case 1: already visited
            if (r, c) in visited:
                return

            # base case 2: out of bound or water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)

        return islands