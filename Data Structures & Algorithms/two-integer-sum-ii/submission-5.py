class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      prevMap = {} 

      for i in range(len(numbers)): 
        difference = target - numbers[i]
        if difference in prevMap: 
          return [prevMap[difference] + 1, i + 1]
        prevMap[numbers[i]] = i
            