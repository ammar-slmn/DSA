class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] 
    
        for p in points: 
            x1 = p[0]
            y1 = p[1] 
            distance = math.sqrt((x1)**2 + (y1)**2)
            print(f"{distance}, {x1}, {y1}")
            minHeap.append([distance, x1, y1])
        
        res = []
        heapq.heapify(minHeap) 
        while len(res) < k: 
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        return res

            
