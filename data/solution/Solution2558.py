import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            max_gifts = max(gifts)
            max_index = gifts.index(max_gifts)
            gifts[max_index] = math.floor(math.sqrt(max_gifts))
        
        return sum(gifts)

def pickGifts(gifts: List[int], k: int) -> int:
    return Solution().pickGifts(gifts, k)