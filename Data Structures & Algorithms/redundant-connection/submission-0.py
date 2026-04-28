class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # edges = [[1,2],[1,3],[3,4],[2,4]]
        adj = {i : [] for i in range(len(edges) + 1)}
        
        def dfs(node, par): 
            # cycle detected 
            if node in visited: 
                return True 
            
            visited.add(node) 

            for nei in adj[node]: 
                if nei == par: 
                    continue 
                if dfs(nei, node): 
                    return True 
            return False 

                
        for u, v in edges: 
            adj[u].append(v) 
            adj[v].append(u)

            print(adj) 

            visited = set() 
            if dfs(u, -1): 
                return [u, v]
        return [] 
