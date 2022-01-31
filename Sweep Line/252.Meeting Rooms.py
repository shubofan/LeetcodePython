"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x.start)

        for i in range(1,len(intervals)):
            if intervals[i].start < intervals[i-1].end:  #### Check Collision condition !!!!!
                return False

        return True