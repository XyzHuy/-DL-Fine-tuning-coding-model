import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        answer = []
        lo, hi = 1, n
        
        # Create the first k-1 elements with the required distinct differences
        for i in range(k - 1):
            if i % 2 == 0:
                answer.append(lo)
                lo += 1
            else:
                answer.append(hi)
                hi -= 1
        
        # Determine the remaining order based on the last element added
        if len(answer) % 2 == 0:
            # If the last added element was from the 'hi' pointer, append the rest in increasing order
            answer.extend(range(lo, hi + 1))
        else:
            # If the last added element was from the 'lo' pointer, append the rest in decreasing order
            answer.extend(range(hi, lo - 1, -1))
        
        return answer

def constructArray(n: int, k: int) -> List[int]:
    return Solution().constructArray(n, k)