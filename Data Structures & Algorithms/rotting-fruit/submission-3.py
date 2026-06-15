class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        rows, cols = len(grid), len(grid[0])
        fresh = set()
        rotten = set()
        queue = deque()
        dirs = [(0,-1),(1,0),(0,1),(-1,0)]

        if not grid: 
            return -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                elif grid[r][c] == 2:
                    rotten.add((r,c))
                    queue.append((r,c))
        if not rotten:
            return -1
        if not fresh:
            return 0

        while queue:
            level_size = len(queue)
            new_rot = False
            for _ in range(level_size):
                r, c = queue.popleft()

                for dir_r, dir_c in dirs:
                    if ((r + dir_r),(c + dir_c)) in fresh:
                        queue.append(((r + dir_r),(c + dir_c)))
                        rotten.add(((r + dir_r),(c + dir_c)))
                        fresh.discard(((r + dir_r),(c + dir_c)))
                        new_rot = True

            if new_rot:
                mins += 1

        if fresh:
            return -1
        return mins