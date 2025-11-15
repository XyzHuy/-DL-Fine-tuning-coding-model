import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Create a sorted list of scores in descending order with their original indices
        sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        
        # Initialize the result list with None
        result = [None] * len(score)
        
        # Assign ranks based on the sorted order
        for rank, (index, _) in enumerate(sorted_scores):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)
        
        return result

def findRelativeRanks(score: List[int]) -> List[str]:
    return Solution().findRelativeRanks(score)