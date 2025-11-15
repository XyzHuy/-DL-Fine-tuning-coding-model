import random
import functools
import collections
import string
import math
import datetime


from typing import List
from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def can_assign(k):
            p = pills
            available_workers = SortedList(workers[-k:])
            for task in tasks[:k][::-1]:
                if not available_workers:
                    return False
                # Try to find a worker who can do the task without a pill
                worker = available_workers.bisect_left(task)
                if worker < len(available_workers):
                    available_workers.pop(worker)
                else:
                    # If no worker can do the task without a pill, use a pill
                    if p == 0:
                        return False
                    p -= 1
                    # Find a worker who can do the task with a pill
                    worker_with_pill = available_workers.bisect_left(task - strength)
                    if worker_with_pill < len(available_workers):
                        available_workers.pop(worker_with_pill)
                    else:
                        return False
            return True
        
        tasks.sort()
        workers.sort()
        left, right = 0, min(len(tasks), len(workers)) + 1
        while left < right:
            mid = (left + right) // 2
            if can_assign(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1

def maxTaskAssign(tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
    return Solution().maxTaskAssign(tasks, workers, pills, strength)