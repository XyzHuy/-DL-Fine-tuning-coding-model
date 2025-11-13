# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def minMeetingRooms(intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    timeline = []
    for interval in intervals:
        # meeting root + 1
        timeline.append((interval.start, 1))
        # meeting root - 1
        timeline.append((interval.end, -1))
    # sort by time
    timeline.sort()
    ans = curr = 0
    # go through timeline
    for _, v in timeline:
        curr += v
        # max meeting room used at this point
        ans = max(ans, curr)
    return ans
