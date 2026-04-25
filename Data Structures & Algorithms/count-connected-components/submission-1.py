class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        links = {i : [] for i in range(n)}
        for n1, n2 in edges: 
            links[n1].append(n2) 
            links[n2].append(n1) 
        
        visited = set()    

        def bfs(node): 
            q = deque() 
            q.append(node) 
            visited.add(node)

            while q: 
                node = q.popleft() 
                for n in links[node]: 
                    if n not in visited: 
                        visited.add(n) 
                        q.append(n) 

        components = 0 
        for node in range(n): 
            if node not in visited: 
                bfs(node)
                components += 1

        return components 
        
        
        