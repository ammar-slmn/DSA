'''
[
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]

problem: 
- heights[r][c] is a height above sea level at the coordinate (r,c) 
- water can only flow to a neighboring cell with height equal or lower. 
    - This means that when traversing the graph, the prev cell needs to be heigher or equal 
        - if height < prevHeight; return 
    - return cells where it can flow into both oceans
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        pac = set() 
        atl = set()

        def bfs(source, ocean): 
            q = deque(source) 
            while q: 
                r, c = q.popleft() 
                ocean.add((r,c)) 

                for dr, dc in DIRECTIONS: 
                    nr, nc = r + dr, c + dc 
                    if (0 <= nr < ROWS and 0 <= nc < COLS and not heights[nr][nc] < heights[r][c] and (nr,nc) not in ocean): 
                        q.append((nr,nc))
        
        pacific = []
        atlantic = [] 
        for c in range(COLS): 
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        for r in range(ROWS): 
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))
        
        bfs(pacific, pac) 
        bfs(atlantic, atl) 
        
        res = []
        for r in range(ROWS): 
            for c in range(COLS): 
                if (r, c) in pac and (r, c) in atl: 
                    res.append([r,c]) 
        return res 

