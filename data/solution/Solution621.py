import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)
        # Find the maximum frequency
        max_count = max(task_counts.values())
        # Count how many tasks have this maximum frequency
        max_count_tasks = sum(1 for count in task_counts.values() if count == max_count)
        
        # Calculate the minimum intervals required
        # (max_count - 1) * (n + 1) is the length of the schedule without the last group of tasks
        # + max_count_tasks is for the last group of tasks (at least one task from each)
        # max(len(tasks), ...) ensures that we do not have less intervals than the number of tasks
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)

def leastInterval(tasks: List[str], n: int) -> int:
    return Solution().leastInterval(tasks, n)