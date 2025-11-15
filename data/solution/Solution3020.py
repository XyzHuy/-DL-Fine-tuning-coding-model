import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Count the frequency of each number in nums
        count = Counter(nums)
        # Initialize the answer to 1, since the smallest valid subset is a single element
        answer = 1
        
        # Handle the special case for 1s separately
        if 1 in count:
            # If there are an odd number of 1s, we can use all of them
            # If there are an even number of 1s, we can use all but one of them
            answer = count[1] if count[1] % 2 == 1 else count[1] - 1
        
        # Check all other numbers
        for num in count:
            if num == 1:
                continue
            current_length = 0
            current_num = num
            # Check the sequence num, num^2, num^4, ...
            while current_num in count:
                if count[current_num] == 1:
                    current_length += 1
                    break
                elif count[current_num] >= 2:
                    current_length += 2
                    current_num *= current_num
                else:
                    break
            # If the sequence length is even, we can only use the first half
            if current_length % 2 == 0:
                current_length -= 1
            # Update the answer with the maximum length found
            answer = max(answer, current_length)
        
        return answer

def maximumLength(nums: List[int]) -> int:
    return Solution().maximumLength(nums)