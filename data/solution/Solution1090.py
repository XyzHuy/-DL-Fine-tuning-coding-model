import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # Combine values and labels into a single list of tuples and sort by value in descending order
        items = sorted(zip(values, labels), reverse=True)
        
        # Dictionary to keep track of the number of items used from each label
        label_count = defaultdict(int)
        
        max_sum = 0
        items_count = 0
        
        # Iterate over the sorted items
        for value, label in items:
            # Check if we can still add items and if the current label has not reached its use limit
            if items_count < numWanted and label_count[label] < useLimit:
                max_sum += value
                label_count[label] += 1
                items_count += 1
            
            # If we have already selected the required number of items, break the loop
            if items_count == numWanted:
                break
        
        return max_sum

def largestValsFromLabels(values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
    return Solution().largestValsFromLabels(values, labels, numWanted, useLimit)