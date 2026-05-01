class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool: 
        if len(edges) > (n - 1): 
            return False 

        adj = {i : [] for i in range(n)}
        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)

        visited = set() 
        def dfs(node, parent): 
            if node in visited: 
                return False

            visited.add(node)

            for n in adj[node]: 
                if node == parent: 
                    continue 
                
        return len(visited) == n