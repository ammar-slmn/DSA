class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        DIRECTIONS = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        visited = set() 
        q = deque()
        distance = 0 

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 0: 
                    q.append((r, c))
                    visited.add((r, c)) 
        
        while q: 
            for i in range(len(q)): 
                r, c = q.popleft() 
                grid[r][c] = distance 

                for dr, dc in DIRECTIONS: 
                    nr, nc = r + dr, c + dc 
                    if (nr < 0 or nr == ROWS or nc < 0 or nc == COLS or (nr, nc) in visited or grid[nr][nc] == -1):
                        continue 
                    
                    visited.add((nr, nc))
                    q.append((nr,nc))

            distance += 1

    