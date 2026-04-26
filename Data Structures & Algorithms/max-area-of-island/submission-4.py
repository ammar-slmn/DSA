class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set() 
        max_area = 0 
        
        def dfs(r, c): 
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited): 
                return 0
            
            area = 1
            visited.add((r, c))

            for dr, dc in directions: 
                area += dfs(dr + r, dc + c) 
            return area 

        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == 1 and (r, c) not in visited: 
                    max_area = max(dfs(r, c), max_area)
        return max_area 
                    