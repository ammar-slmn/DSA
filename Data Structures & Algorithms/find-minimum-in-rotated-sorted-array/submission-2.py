"""
nums = [3,4,5,6,1,2]
- return 1 

nums = [4,5,6,7]
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 
        res = nums[-1]

        while l <= r: 
            if nums[l] < nums[r]: 
                res = min(nums[l], res) 
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])

            print("num at m: ", nums[m])
            print("num at l: ", nums[l])
            print("num at r: ", nums[r])

            if nums[m] > nums[l]: 
                l = m + 1 
            else: 
                r = m - 1 

        return res 

    