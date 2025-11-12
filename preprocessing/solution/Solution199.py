# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x.start)
    ls = len(intervals)
    for i in range(ls - 1):
        if intervals[i].end > intervals[i + 1].start:
            return False
    return True
