class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {} # num : index 

        for i in range(len(nums)): 
            diff = target - nums[i]
            if diff in indexMap:
                return [indexMap[diff], i]
            else:
                indexMap[nums[i]] = i
