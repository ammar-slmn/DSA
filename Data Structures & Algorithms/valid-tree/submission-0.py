class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool: 
        # {0: [1], 1: [2, 3, 4], 2: [3], 3: [], 4: []}
        if len(edges) > (n - 1): 
            return False 

        adj = {i : [] for i in range(n)}
        for u, v in edges: 
            adj[u].append(v) 

        visiting = set() 
    
        def dfs(node): 

            if node in visiting: 
                return False 
            
            if adj[node] == []: 
                return True 

            visiting.add(node) 

            for nei in adj[node]: 
                if not dfs(nei): 
                    return False 
            
            visiting.remove(node) 
            return True 

        for node in range(n): 
            if not dfs(node): 
                return False 
        
        return True 