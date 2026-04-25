class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set() 
        maximum_area = 0

        def bfs(r, c): 
            q = deque() 
            visited.add((r, c))
            q.append((r, c))
            area = 1 

            while q: 
                row, col = q.popleft() 
                for dr, dc in DIRECTIONS: 
                    nr, nc = dr + row, dc +  col
                    if (nc < 0 or nr < 0 or nc >= COLS or nr >= ROWS or (nr, nc) in visited or grid[nr][nc] == 0): 
                        continue 
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    area += 1 
            return area 

        for r in range(ROWS): 
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited: 
                    maximum_area = max(maximum_area, bfs(r, c)) 

        return maximum_area