import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # Initialize the count of triplets
        count = 0
        n = len(arr)
        
        # Iterate over all possible starting points i
        for i in range(n):
            xor_sum = 0
            # Iterate over all possible ending points k
            for k in range(i, n):
                # Calculate the xor from i to k
                xor_sum ^= arr[k]
                # If xor_sum is 0, it means we found valid (i, j, k) triplets
                # where a == b, and there are (k - i) such triplets
                if xor_sum == 0:
                    count += (k - i)
        
        return count

def countTriplets(arr: List[int]) -> int:
    return Solution().countTriplets(arr)