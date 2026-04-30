"""
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output = False

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1

        while top <= bottom: 
            row = (top + bottom) // 2 
            if target > matrix[row][-1]: 
                top = row + 1 
            elif target < matrix[row][0]: 
                bottom = row - 1 
            else: 
                break 

        # row is our index 
        row = (top + bottom) // 2
        print("top: ", top)
        print("bottom: ", bottom)
        print("row: ", row)
        l, r = 0, cols - 1
        while l <= r: 
            m = (l + r) // 2
            print("this is the middle: ", m)
            if target > matrix[row][m]: 
                l = m + 1 
            elif target < matrix[row][m]: 
                r = m - 1
            else: 
                return True 
        return False 
                
            
        
