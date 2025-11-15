import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Calculate the initial sum of the first k cards
        total = sum(cardPoints[:k])
        max_score = total
        
        # Slide the window from the end of the array to the start
        for i in range(1, k + 1):
            # Subtract the element that is left out of the window and add the new element
            total += cardPoints[-i] - cardPoints[k - i]
            max_score = max(max_score, total)
        
        return max_score

def maxScore(cardPoints: List[int], k: int) -> int:
    return Solution().maxScore(cardPoints, k)