import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Count the frequency of each number in nums
        count = Counter(nums)
        # This will keep track of the end of subsequences
        end = Counter()
        
        for num in nums:
            if count[num] == 0:
                # If there are no more of this number, skip
                continue
            elif end[num - 1] > 0:
                # If a subsequence can be extended by this number
                end[num - 1] -= 1
                end[num] += 1
            elif count[num + 1] > 0 and count[num + 2] > 0:
                # If a new subsequence can be started with this number and the next two
                count[num + 1] -= 1
                count[num + 2] -= 1
                end[num + 2] += 1
            else:
                # If neither extending a subsequence nor starting a new one is possible
                return False
            count[num] -= 1
        
        return True

def isPossible(nums: List[int]) -> bool:
    return Solution().isPossible(nums)