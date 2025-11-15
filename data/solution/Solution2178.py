import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []  # If finalSum is odd, it cannot be split into even integers
        
        result = []
        current_even = 2
        
        while finalSum >= current_even:
            result.append(current_even)
            finalSum -= current_even
            current_even += 2
        
        # If there's any remaining sum, add it to the last element
        if finalSum > 0:
            result[-1] += finalSum
        
        return result

def maximumEvenSplit(finalSum: int) -> List[int]:
    return Solution().maximumEvenSplit(finalSum)