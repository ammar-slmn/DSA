class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()

        def dfs(r, c): 
            if (
                r < 0 or r not in range(rows) 
                or c < 0 or c not in range(cols) 
                or grid[r][c] == 0 
            ): 
                return 1

            if (r, c) in visited: 
                return 0 

            visited.add((r,c))

            perimeter = 0 
            for dr, dc in directions: 
                perimeter += dfs(r + dr, c + dc)
            
            return perimeter 

        
        for r in range(rows):
            for c in range(cols): 
                return dfs(r, c)
        