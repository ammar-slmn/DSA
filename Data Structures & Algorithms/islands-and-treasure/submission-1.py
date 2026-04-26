class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        DIRECTIONS = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0]) 
        visited = set() 
        INF = 2147483647

        def dfs(r, c): 
            if (r < 0 or r not in range(ROWS) or c < 0 or c not in range(COLS) or grid[r][c] == -1 or (r, c) in visited):
                return INF 

            if grid[r][c] == 0: 
                return 0 

            visited.add((r, c))

            res = INF
            for dr, dc in DIRECTIONS: 
                res = min(res, 1 + dfs(r + dr, c + dc)) 

            visited.remove((r, c)) # backtracking 
            return res 


        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == INF: 
                    grid[r][c] = dfs(r, c)
    