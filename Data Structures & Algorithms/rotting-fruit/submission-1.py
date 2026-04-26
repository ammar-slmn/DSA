class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0],[0, -1]]
        visited = set() 
        fresh = 0
        q = deque() 

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1: 
                    fresh += 1
                if grid[r][c] == 2: 
                    q.append((r, c)) 

        minutes = 0
        while fresh > 0 and q: 
            for _ in range(len(q)): 
                r, c = q.popleft() 
                visited.add((r, c))

                for dr, dc in directions: 
                    nr, nc = dr + r, dc + c
                    if (
                        nr < 0 or nc < 0 
                        or nr not in range(rows) 
                        or nc not in range(cols) 
                        or grid[nr][nc] != 1
                        or (nr, nc) in visited
                    ): 
                        continue 
                    grid[nr][nc] == 2
                    visited.add((nr, nc)) 
                    q.append((nr, nc))
                    fresh -= 1
            minutes += 1

        if fresh != 0: 
            return -1 
        return minutes 