import collections
import string
import math
import datetime


class Solution:
    def countSegments(self, s: str) -> int:
        # Split the string by spaces and filter out any empty strings
        segments = s.split()
        # Return the number of non-empty segments
        return len(segments)

def countSegments(s: str) -> int:
    return Solution().countSegments(s)