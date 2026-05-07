"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        n = len(intervals)-1
        for i, interval in enumerate(intervals):
            if i!=n: 
                if interval.end >intervals[i+1].start:
                    return False
        return True