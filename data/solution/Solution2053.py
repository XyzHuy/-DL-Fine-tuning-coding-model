import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Count the occurrences of each string in the array
        count = Counter(arr)
        
        # Filter out the distinct strings (those that appear only once)
        distinct_strings = [s for s in arr if count[s] == 1]
        
        # Return the k-th distinct string if it exists, otherwise return an empty string
        return distinct_strings[k-1] if k <= len(distinct_strings) else ""

def kthDistinct(arr: List[str], k: int) -> str:
    return Solution().kthDistinct(arr, k)