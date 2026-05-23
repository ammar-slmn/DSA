"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# intervals = [(0,40),(5,10),(15,20)]

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i : i.start)
        rooms = 1 

        for i in range(1, len(intervals)): 
            if intervals[i].start < intervals[i - 1].end: 
                rooms += 1
        return rooms

