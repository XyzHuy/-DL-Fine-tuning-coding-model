import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Create a list to store the count of remainders
        remainder_count = [0] * 60
        pair_count = 0
        
        for t in time:
            # Calculate the remainder of the current song duration when divided by 60
            remainder = t % 60
            
            # Find the complement remainder that would make the sum divisible by 60
            complement = (60 - remainder) % 60
            
            # Add the count of the complement remainder to the pair count
            pair_count += remainder_count[complement]
            
            # Update the count of the current remainder
            remainder_count[remainder] += 1
        
        return pair_count

def numPairsDivisibleBy60(time: List[int]) -> int:
    return Solution().numPairsDivisibleBy60(time)