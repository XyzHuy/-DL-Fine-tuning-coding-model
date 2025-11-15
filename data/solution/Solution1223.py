import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(remaining, last_face, last_count):
            if remaining == 0:
                return 1
            
            total_sequences = 0
            for face in range(6):
                if face == last_face:
                    if last_count + 1 <= rollMax[face]:
                        total_sequences += dp(remaining - 1, face, last_count + 1)
                else:
                    total_sequences += dp(remaining - 1, face, 1)
            
            return total_sequences % MOD
        
        return dp(n, -1, 0)

def dieSimulator(n: int, rollMax: List[int]) -> int:
    return Solution().dieSimulator(n, rollMax)