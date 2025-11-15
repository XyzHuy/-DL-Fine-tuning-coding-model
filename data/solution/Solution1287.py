import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # Calculate the threshold for 25% of the array length
        threshold = len(arr) // 4
        
        # Count the occurrences of each number in the array
        count = Counter(arr)
        
        # Find the number that occurs more than 25% of the time
        for num, freq in count.items():
            if freq > threshold:
                return num

def findSpecialInteger(arr: List[int]) -> int:
    return Solution().findSpecialInteger(arr)