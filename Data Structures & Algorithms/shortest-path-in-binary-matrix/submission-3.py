class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        current_len = 1
        rows, cols = len(grid), len(grid[0])

        visited = set()
        visited.add((0,0)) # [(0, -1)]

        queue = deque()
        queue.append((0,0,current_len)) # [(0, -1)]

        if grid[0][0] == 1:
            return -1

        dirs = [(-1, 0), (-1, 1), (0,1), (1,1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        while queue:
            curr = queue.popleft() # (0,0)
            # edge case 1: reached bottom right of matrix
            if curr[0] == (rows - 1) and curr[1] == (cols - 1):
                return curr[2]

            r, c, current_len = curr # 0, 0
            for dr, dc in dirs:
                # edge case two: out of bounds
                if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
                    continue

                # edge case three: invalid cell value
                elif grid[r + dr][c + dc] != 0:
                    continue

                elif ((r + dr), (c + dc)) in visited:
                    continue

                visited.add(((r + dr), (c + dc)))
                queue.append(((r + dr), (c + dc), (current_len + 1)))

        return -1