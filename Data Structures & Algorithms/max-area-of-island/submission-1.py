class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set() 
        maximum_area = 0

        def dfs(r, c): 
            if (r == ROWS or c == COLS or r < 0 or c < 0 or grid[r][c] == 0 or (r, c) in visited): 
                return 0 
            
            area = 1
            visited.add((r, c))
            for dr, dc in DIRECTIONS: 
                area += dfs(r + dr, c + dc)
            return area 

        for r in range(ROWS): 
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited: 
                    maximum_area = max(maximum_area, dfs(r, c)) 

        return maximum_area