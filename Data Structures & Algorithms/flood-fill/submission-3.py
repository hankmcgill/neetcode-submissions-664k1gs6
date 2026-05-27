class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        if starting_color == color:
            return image

        def dfs(r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            
            if image[r][c] != starting_color:
                return

            image[r][c] = color

            # recurse down one row
            dfs (r + 1, c)
            # recurse up one row
            dfs (r - 1, c)
            # recurse left one column
            dfs (r, c - 1)
            # recurse right one column
            dfs (r, c + 1)

        dfs(sr, sc)
        return image