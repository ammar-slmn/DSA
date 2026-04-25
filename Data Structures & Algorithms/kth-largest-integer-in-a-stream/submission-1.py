class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.array = nums

    def add(self, val: int) -> int: 
        self.array.append(val) 
        self.array.sort()
        # [1, 2, 3, 4, 5, 6]
        return self.array[len(self.array) - self.k]
