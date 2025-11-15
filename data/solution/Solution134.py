import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = j = n - 1
        cnt = s = 0
        while cnt < n:
            s += gas[j] - cost[j]
            cnt += 1
            j = (j + 1) % n
            while s < 0 and cnt < n:
                i -= 1
                s += gas[i] - cost[i]
                cnt += 1
        return -1 if s < 0 else i

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    return Solution().canCompleteCircuit(gas, cost)