import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        # Sort jobs and workers to pair the smallest job with the smallest capacity worker, and so on.
        jobs.sort()
        workers.sort()
        
        # Calculate the maximum days required by any worker to complete their assigned job.
        max_days = 0
        for job, worker in zip(jobs, workers):
            # Calculate days needed for the current worker to complete the current job
            days = math.ceil(job / worker)
            # Update the maximum days required
            max_days = max(max_days, days)
        
        return max_days

def minimumTime(jobs: List[int], workers: List[int]) -> int:
    return Solution().minimumTime(jobs, workers)