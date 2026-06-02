class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cols, rows = len(image[0]), len(image)

        if image[sr][sc] == color:
            return image

        starting_color = image[sr][sc]

        # run dfs on image
        def dfs (r, c):
            # edge case 1: out of bounds
            if r >= rows or c >= cols or r < 0 or c < 0:
                return
            # edge case 2: color at coords is already correct
            if image[r][c] != starting_color:
                return

            # reassign color at coords
            image[r][c] = color

            # recursively travel n,s,e,w
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image