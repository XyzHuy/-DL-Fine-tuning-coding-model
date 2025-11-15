import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # Convert hours to a list of 1s and -1s where 1 represents a tiring day and -1 represents a non-tiring day
        score = [1 if h > 8 else -1 for h in hours]
        
        # Dictionary to store the first occurrence of each prefix sum
        prefix_sum_index = {}
        prefix_sum = 0
        max_length = 0
        
        for i, s in enumerate(score):
            prefix_sum += s
            
            # If the prefix sum is positive, the interval from the start to the current day is well-performing
            if prefix_sum > 0:
                max_length = i + 1
            else:
                # If the prefix sum is not positive, check if there is a previous prefix sum that is less than the current prefix sum - 1
                if prefix_sum - 1 in prefix_sum_index:
                    max_length = max(max_length, i - prefix_sum_index[prefix_sum - 1])
                
                # Store the first occurrence of the prefix sum
                if prefix_sum not in prefix_sum_index:
                    prefix_sum_index[prefix_sum] = i
        
        return max_length

def longestWPI(hours: List[int]) -> int:
    return Solution().longestWPI(hours)