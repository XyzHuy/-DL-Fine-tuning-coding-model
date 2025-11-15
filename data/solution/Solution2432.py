import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_time = logs[0][1]
        result_id = logs[0][0]
        
        for i in range(1, len(logs)):
            current_time = logs[i][1] - logs[i - 1][1]
            if current_time > max_time or (current_time == max_time and logs[i][0] < result_id):
                max_time = current_time
                result_id = logs[i][0]
        
        return result_id

def hardestWorker(n: int, logs: List[List[int]]) -> int:
    return Solution().hardestWorker(n, logs)