class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0 
        
        rows, cols = len(grid), len(grid[0])
        visited = set() 
        islands = 0 
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
        def dfs(r, c): 
            if (r < 0 or r not in range(rows) or c < 0 or c not in range(cols) or grid[r][c] == "0" or (r, c) in visited):
                return 
            
            visited.add((r, c))
            for dr, dc in DIRECTIONS: 
                nr, nc = dr + r, dc + c 
                dfs(nr, nc)


        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == "1" and (r, c) not in visited: 
                    dfs(r, c)
                    islands +=1 
        return islands 