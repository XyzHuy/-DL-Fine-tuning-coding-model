import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # Convert times to minutes since the start of the day for easier comparison
        def time_to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        start1 = time_to_minutes(event1[0])
        end1 = time_to_minutes(event1[1])
        start2 = time_to_minutes(event2[0])
        end2 = time_to_minutes(event2[1])
        
        # Check for overlap
        return not (end1 < start2 or end2 < start1)

def haveConflict(event1: List[str], event2: List[str]) -> bool:
    return Solution().haveConflict(event1, event2)