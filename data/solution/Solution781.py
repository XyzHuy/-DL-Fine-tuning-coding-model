import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Count the occurrences of each answer
        answer_counts = Counter(answers)
        
        # Calculate the minimum number of rabbits
        min_rabbits = 0
        for answer, count in answer_counts.items():
            # Each group of (answer + 1) rabbits will have the same answer
            # We need to round up to the nearest multiple of (answer + 1)
            min_rabbits += (count + answer) // (answer + 1) * (answer + 1)
        
        return min_rabbits

def numRabbits(answers: List[int]) -> int:
    return Solution().numRabbits(answers)