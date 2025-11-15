import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Combine difficulty and profit into a list of tuples and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        
        # Create a list to store the maximum profit up to each difficulty
        max_profits = []
        current_max_profit = 0
        for job in jobs:
            current_max_profit = max(current_max_profit, job[1])
            max_profits.append(current_max_profit)
        
        # Sort the workers' abilities
        worker.sort()
        
        # Two pointers to find the best job for each worker
        total_profit = 0
        job_index = 0
        n = len(jobs)
        
        for ability in worker:
            # Find the highest difficulty job that the worker can do
            while job_index < n and jobs[job_index][0] <= ability:
                job_index += 1
            # If job_index is not 0, the previous job is the best the worker can do
            if job_index > 0:
                total_profit += max_profits[job_index - 1]
        
        return total_profit

def maxProfitAssignment(difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    return Solution().maxProfitAssignment(difficulty, profit, worker)