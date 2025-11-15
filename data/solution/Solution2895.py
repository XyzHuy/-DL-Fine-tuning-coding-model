import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        ans = 0
        i = len(tasks) - 1
        for t in processorTime:
            ans = max(ans, t + tasks[i])
            i -= 4
        return ans

def minProcessingTime(processorTime: List[int], tasks: List[int]) -> int:
    return Solution().minProcessingTime(processorTime, tasks)