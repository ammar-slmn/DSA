class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            # find the area
            area = min(heights[l], heights[r]) * (r - l)
            # find the max
            res = max(area, res)
            # if the left pointer height is less or equal than right, move left up
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res