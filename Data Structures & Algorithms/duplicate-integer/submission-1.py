class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setOfExistingNums = set()
        for x in nums: 
            if x in setOfExistingNums: 
                return True
            else: 
                setOfExistingNums.add(x)
        return False 
