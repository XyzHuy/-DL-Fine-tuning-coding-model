import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Count the occurrences of each value in the array
        occurrences = Counter(arr).values()
        # Check if the number of occurrences is unique
        return len(occurrences) == len(set(occurrences))

def uniqueOccurrences(arr: List[int]) -> bool:
    return Solution().uniqueOccurrences(arr)