class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int
    ) -> List[List[int]]:

        starting_color = image[sr][sc]

        # Important edge case:
        # if the new color is the same as the old one,
        # recursion would loop forever.
        if starting_color == color:
            return image

        def dfs(r, c):
            # out of bounds
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return

            # stop if this cell is not the original color
            if image[r][c] != starting_color:
                return

            # recolor the cell
            image[r][c] = color

            # recurse in 4 directions
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        dfs(sr, sc)
        return image