class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        rows = len(image)
        cols = len(image[0])
        dirs = [1, 0, -1, 0, 1]

        def dfs(r, c, pix):
            if not (0 <= r < rows) or not (0 <= c < cols) or image[r][c] != pix:
                return

            image[r][c] = color
            for d in range(4):
                dfs(r + dirs[d], c + dirs[d + 1], pix)

        dfs(sr, sc, image[sr][sc])
        return image