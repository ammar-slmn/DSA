class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        DIRECTIONS = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(r, c): 
            q = deque() 
            visited = set()
            q.append((r, c))
            visited.add((r,c))
            count = 0 

            while q: 
                for _ in range(len(q)): 
                    row, col = q.popleft() 
                    if grid[row][col] == 0: 
                        return count
                    for dr, dc in DIRECTIONS: 
                        nr, nc = row + dr, col + dc 
                        if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] != -1): 
                            visited.add((nr, nc))
                            q.append((nr, nc))
                count += 1 
            
            return INF 


        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == INF: 
                    grid[r][c] = bfs(r, c)
    