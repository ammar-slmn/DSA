class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [-1,0,2,4,6,8]

        l = 0 
        r = len(nums)

        while l < r: 
            m = (r - l) // 2
            if nums[m] < target: 
                l = m + 1 
            if nums[m] > target: 
                r = m - 1 
            elif nums[m] == target: 
                return m 
            return -1
