import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # Check for Flush
        if len(set(suits)) == 1:
            return "Flush"
        
        # Count the occurrences of each rank
        rank_counts = Counter(ranks)
        
        # Check for Three of a Kind
        if any(count >= 3 for count in rank_counts.values()):
            return "Three of a Kind"
        
        # Check for Pair
        if any(count == 2 for count in rank_counts.values()):
            return "Pair"
        
        # If none of the above, it's a High Card
        return "High Card"

def bestHand(ranks: List[int], suits: List[str]) -> str:
    return Solution().bestHand(ranks, suits)