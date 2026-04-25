class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i in range(len(nums)): 
          val = target - nums[i]
          if val in diff_map: 
            return [diff_map[val], i]
          diff_map[nums[i]] = i 