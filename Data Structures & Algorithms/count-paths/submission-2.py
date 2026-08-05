class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def get_paths(r, c, rows, cols, cache):
            if r == rows or c == cols:
                return 0

            if cache[r][c] > 0:
                return cache[r][c]

            if r == rows - 1 or c == cols - 1:
                return 1

            cache[r][c] = (
                get_paths(r + 1, c, rows, cols, cache)
                + get_paths(r, c + 1, rows, cols, cache)
            )

            return cache[r][c]

        cache = [[0] * n for _ in range(m)]
        return get_paths(0, 0, m, n, cache)