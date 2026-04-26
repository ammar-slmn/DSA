class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool: 
        if len(edges) > (n - 1): 
            return False 

        adj = {i : [] for i in range(n)}
        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)

        q = deque() 
        q.append((0, -1))
        visited = set() 

        while q: 
            node, parent = q.popleft() 
            visited.add(node)
            
            for neighbor in adj[node]: 
                if neighbor == parent: 
                    continue 
                if neighbor in visited: 
                    return False 
                visited.add(neighbor)
                q.append((neighbor, node))
        
        return len(visited) == n 
        
