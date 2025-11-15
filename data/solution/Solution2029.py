import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # Count the number of stones with values % 3 == 0, 1, 2
        count = [0, 0, 0]
        for stone in stones:
            count[stone % 3] += 1
        
        # If there are no stones with value % 3 == 0, the game reduces to a simple parity check
        if count[0] % 2 == 0:
            # If count[0] is even, Alice can always mirror Bob's moves
            # Alice wins if there are both stones with value % 3 == 1 and value % 3 == 2
            return count[1] > 0 and count[2] > 0
        else:
            # If count[0] is odd, Alice can only win if the difference between count[1] and count[2] is more than 2
            # This is because she can force Bob into a losing position by using the odd count of 0s to balance the game
            return abs(count[1] - count[2]) > 2

def stoneGameIX(stones: List[int]) -> bool:
    return Solution().stoneGameIX(stones)