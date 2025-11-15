import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def countBits(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count
        
        result = []
        for hour in range(12):
            for minute in range(60):
                if countBits(hour) + countBits(minute) == turnedOn:
                    result.append(f"{hour}:{minute:02}")
        return result

def readBinaryWatch(turnedOn: int) -> List[str]:
    return Solution().readBinaryWatch(turnedOn)