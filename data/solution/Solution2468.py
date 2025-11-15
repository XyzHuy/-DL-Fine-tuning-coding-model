import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        def can_split_into_parts(k):
            # Calculate the total length required if we split the message into k parts
            total_length = 0
            digits_in_k = len(str(k))
            for i in range(1, k + 1):
                # Length of the suffix <i/k>
                suffix_length = 3 + len(str(i)) + digits_in_k
                if limit <= suffix_length:
                    return False
                total_length += limit - suffix_length
            return total_length >= len(message)
        
        # Binary search to find the minimum number of parts
        left, right = 1, len(message) + 1
        while left < right:
            mid = (left + right) // 2
            if can_split_into_parts(mid):
                right = mid
            else:
                left = mid + 1
        
        # If no valid number of parts is found, return an empty list
        if left > len(message):
            return []
        
        # Now, split the message into 'left' parts
        parts = []
        index = 0
        digits_in_left = len(str(left))
        for i in range(1, left + 1):
            suffix = f"<{i}/{left}>"
            part_length = limit - len(suffix)
            parts.append(message[index:index + part_length] + suffix)
            index += part_length
        
        return parts

def splitMessage(message: str, limit: int) -> List[str]:
    return Solution().splitMessage(message, limit)