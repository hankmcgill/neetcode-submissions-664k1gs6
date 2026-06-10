class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        shortest = 0
        rows, cols = len(grid), len(grid[0])

        visited = set((0,0))
        visited.add((0,0)) # [(0, -1)]

        queue = deque()
        queue.append((0,0)) # [(0, -1)]

        dirs = [(-1, 0), (-1, -1), (0,1), (1,1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        while queue:
            curr = queue.popleft() # (0,0)
            # edge case 1: reached bottom right of matrix
            if curr == ((rows - 1), (cols - 1)):
                return shortest

            r, c = curr # 0, 0
            for dr, dc in dirs:
                # edge case two: out of bounds
                if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
                    continue

                # edge case three: invalid cell value
                elif grid[r + dr][c + dc] != 0:
                    continue

                visited.add(((r + dr), (c + dc)))
                queue.append(((r + dr), (c + dc)))

                shortest += 1

        return -1