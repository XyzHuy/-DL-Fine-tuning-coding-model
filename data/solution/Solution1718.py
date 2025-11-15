import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def backtrack(pos):
            if pos == length:
                return True
            if sequence[pos] != 0:
                return backtrack(pos + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1:
                    sequence[pos] = num
                    used[num] = True
                    if backtrack(pos + 1):
                        return True
                    used[num] = False
                    sequence[pos] = 0
                elif pos + num < length and sequence[pos + num] == 0:
                    sequence[pos] = sequence[pos + num] = num
                    used[num] = True
                    if backtrack(pos + 1):
                        return True
                    used[num] = False
                    sequence[pos] = sequence[pos + num] = 0
            return False
        
        length = 2 * n - 1
        sequence = [0] * length
        used = [False] * (n + 1)
        backtrack(0)
        return sequence

def constructDistancedSequence(n: int) -> List[int]:
    return Solution().constructDistancedSequence(n)