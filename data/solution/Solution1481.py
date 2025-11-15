import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Count the frequency of each number in the array
        count = Counter(arr)
        
        # Sort the items by their frequency
        sorted_count = sorted(count.items(), key=lambda x: x[1])
        
        # Initialize the number of unique integers
        unique_count = len(sorted_count)
        
        # Iterate over the sorted items
        for num, freq in sorted_count:
            if k >= freq:
                # If k is greater than or equal to the frequency of the current number
                # We can remove all occurrences of this number
                k -= freq
                unique_count -= 1
            else:
                # If k is less than the frequency of the current number
                # We cannot remove all occurrences, so we stop here
                break
        
        return unique_count

def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
    return Solution().findLeastNumOfUniqueInts(arr, k)