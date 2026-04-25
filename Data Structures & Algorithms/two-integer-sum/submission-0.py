class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(len(nums)):
            # re-arrange equation to nums[j] = target - nums[i]
            indices.append(i)
            for j in range(len(nums)):
                if nums[j] == target - nums[i]:
                    indices.append(j)
                    return indices

