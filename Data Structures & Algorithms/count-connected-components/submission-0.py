class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        links = {i : [] for i in range(n)}
        for n1, n2 in edges: 
            links[n1].append(n2) 
            links[n2].append(n1) 
        
        visited = set()    

        def dfs(node):
            visited.add(node) 

            for neighbor in links[node]: 
                if neighbor not in visited: 
                    dfs(neighbor)


        components = 0 
        for node in range(n): 
            if node not in visited: 
                dfs(node) 
                components += 1 
        return components 
        
        
        