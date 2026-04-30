class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1: 
            x = max(stones) 
            stones.remove(x) 
            y = max(stones)
            stones.remove(y) 
            if x == y: 
                continue
            else: 
                res = x - y 
                stones.append(res) 
        if stones: 
            return stones[0]
        return 0 