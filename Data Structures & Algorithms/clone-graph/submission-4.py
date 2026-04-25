"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None 
        
        cloneMap = {}
        q = deque() 
        q.append(node)
        copy = Node(node.val)
        cloneMap[node] = copy 

        while q: 
            cur = q.popleft() 
            for n in cur.neighbors: 
                if n not in cloneMap: 
                    n_copy = Node(n.val)
                    cloneMap[n] = n_copy 
                    q.append(n) 
                cloneMap[cur].neighbors.append(cloneMap[n])
        return cloneMap[node]