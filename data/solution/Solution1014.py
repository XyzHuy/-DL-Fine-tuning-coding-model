import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Initialize the maximum score with the first possible pair
        max_score = values[0] + values[1] + 0 - 1
        # Initialize the best value of values[i] + i seen so far
        best_i = values[0] + 0
        
        # Iterate over the array starting from the second element
        for j in range(1, len(values)):
            # Calculate the score for the current pair (best_i, j)
            current_score = best_i + values[j] - j
            # Update the maximum score if the current score is higher
            max_score = max(max_score, current_score)
            # Update the best value of values[i] + i seen so far
            best_i = max(best_i, values[j] + j)
        
        return max_score

def maxScoreSightseeingPair(values: List[int]) -> int:
    return Solution().maxScoreSightseeingPair(values)