class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i : i[0])
        output = [intervals[0]]
        count = 0

        for start, end in intervals: 
            lastEnd = output[-1][1]

            if start < lastEnd: 
                output.pop()
