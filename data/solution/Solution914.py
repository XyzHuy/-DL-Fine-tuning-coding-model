import random
import functools
import collections
import string
import math
import datetime


from math import gcd
from functools import reduce
from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Count the occurrences of each card
        counts = list(sorted(set(deck)))
        counts = [deck.count(card) for card in counts]
        
        # Compute the GCD of all counts
        def find_gcd(list_of_numbers):
            x = reduce(gcd, list_of_numbers)
            return x
        
        # Get the GCD of the counts
        gcd_of_counts = find_gcd(counts)
        
        # Check if the GCD is greater than 1
        return gcd_of_counts > 1

def hasGroupsSizeX(deck: List[int]) -> bool:
    return Solution().hasGroupsSizeX(deck)