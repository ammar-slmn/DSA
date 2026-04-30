"""
Input: piles = [1,4,3,2], h = 9
output = 2 
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) # maximum speed 
        res = r 
        
        while l <= r: 
            mid = (l + r) // 2
            totalTime = 0 

            for p in piles: 
                totalTime += math.ceil(float(p) / mid)
            if totalTime <= h: 
                res = mid
                r = mid - 1
            else: 
                l = mid + 1 
        return res 
