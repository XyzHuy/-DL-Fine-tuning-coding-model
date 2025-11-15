import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        # Initialize the number of partitions to 0
        partitions = 0
        # Initialize the current number as an empty string
        current_number = ""
        
        for digit in s:
            # Try to add the current digit to the current number
            if int(current_number + digit) <= k:
                current_number += digit
            else:
                # If adding the digit makes the number greater than k,
                # we need to start a new partition
                partitions += 1
                current_number = digit
            
            # If at any point a single digit is greater than k, return -1
            if int(digit) > k:
                return -1
        
        # If there's any remaining number, it counts as a partition
        if current_number:
            partitions += 1
        
        return partitions

def minimumPartition(s: str, k: int) -> int:
    return Solution().minimumPartition(s, k)