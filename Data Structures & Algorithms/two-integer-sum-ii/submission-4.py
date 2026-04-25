class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      prevMap = {} 

      for i in range(1, len(numbers)): 
        difference = target - numbers[i - 1]
        if difference in prevMap: 
          return [prevMap[difference], i]
        prevMap[numbers[i - 1]] = i
            