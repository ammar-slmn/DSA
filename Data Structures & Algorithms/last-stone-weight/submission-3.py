class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1: 
            stones.sort() 
            new_weight = stones.pop() - stones.pop() 
            if new_weight: 
                stones.append(new_weight) 

        if stones: 
            return stones[0]
        else: 
            return 0