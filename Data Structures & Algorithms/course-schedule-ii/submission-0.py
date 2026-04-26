class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}


        for u, v in prerequisites: 
            adj[u].append(v) 
        
        cycle, visit = set(), set() 
        res = []

        print(adj) # {0: [1], 1: [2], 2: [0]}

        def dfs(crs): 
            if crs in cycle: 
                return False 
                
            if crs in visit: 
                return True 

            cycle.add(crs) 
            for pre in adj[crs]: 
                if not dfs(pre): 
                    return False 
            cycle.remove(crs) 
            visit.add(crs) 
            res.append(crs) 
            return True 

        for c in range(numCourses): 
            if not dfs(c): 
                return [] 
        return res  