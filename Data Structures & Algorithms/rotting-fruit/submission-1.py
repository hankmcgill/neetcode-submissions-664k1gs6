from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        rows, cols = len(grid), len(grid[0])

        fresh = set()
        queue = deque()
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        if not grid:
            return -1

        # Find all fresh and initially rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    queue.append((r, c))

        # If there are no fresh oranges, we're already done
        if not fresh:
            return 0

        while queue:
            level_size = len(queue)
            new_rot = False

            for _ in range(level_size):
                r, c = queue.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if (nr, nc) in fresh:
                        fresh.remove((nr, nc))
                        queue.append((nr, nc))
                        new_rot = True

            if new_rot:
                mins += 1

        if fresh:
            return -1

        return mins