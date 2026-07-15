"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda meeting: meeting.start)
        n = len(intervals)
        for i, meeting in enumerate(intervals):
            if i < n-1 and meeting.end > intervals[i+1].start:
                return False
        return True