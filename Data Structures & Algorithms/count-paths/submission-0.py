class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def get_paths(m, n, rows, cols, cache):
            if m == rows or n == cols:
                return 0
            if cache[m][n] > 0:
                return cache[m][n]
            if m == (rows - 1) or n == (cols - 1):
                return 1
    
            cache[m][n] = (get_paths(m + 1, n, rows, cols, cache) + 
            get_paths(m, n + 1, rows, cols, cache))

            return cache[m][n]

        return get_paths(0, 0, m, n, [[0] * n for i in range(m)])