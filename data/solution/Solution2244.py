import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # Count the frequency of each task difficulty
        task_counts = Counter(tasks)
        rounds = 0
        
        for count in task_counts.values():
            # If there is only one task of a certain difficulty, it's impossible to complete it
            if count == 1:
                return -1
            # Calculate the minimum rounds needed for tasks of the same difficulty
            # We prioritize completing 3 tasks at a time
            rounds += count // 3
            # If there are remaining tasks (1 or 2), we need one more round
            if count % 3 != 0:
                rounds += 1
        
        return rounds

def minimumRounds(tasks: List[int]) -> int:
    return Solution().minimumRounds(tasks)