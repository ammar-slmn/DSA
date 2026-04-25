class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1: 
            stones.sort() 
            result = stones.pop() - stones.pop() 
            if result: 
                stones.append(result)
        if stones: 
            return stones[0]
        else: 
            return 0 