"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        timeScheduled = []

        for i in intervals: 
            time = range(i.start, i.end)
            for t in time: 
                if t in timescheduled: 
                    return False 
                else: 
                    timeScheduled.append
        return True 