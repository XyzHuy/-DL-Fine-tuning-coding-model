import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Create a dictionary to store the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        # Initialize variables to keep track of the current partition
        start, end = 0, 0
        partitions = []
        
        # Iterate over the string
        for idx, char in enumerate(s):
            # Update the end of the current partition to the last occurrence of the current character
            end = max(end, last_occurrence[char])
            
            # If we are at the end of the current partition, add its length to the partitions list
            if idx == end:
                partitions.append(end - start + 1)
                start = idx + 1
        
        return partitions

def partitionLabels(s: str) -> List[int]:
    return Solution().partitionLabels(s)