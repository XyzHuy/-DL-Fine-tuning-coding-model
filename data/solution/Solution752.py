import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def next(s):
            res = []
            s = list(s)
            for i in range(4):
                c = s[i]
                s[i] = '9' if c == '0' else str(int(c) - 1)
                res.append(''.join(s))
                s[i] = '0' if c == '9' else str(int(c) + 1)
                res.append(''.join(s))
                s[i] = c
            return res

        if target == '0000':
            return 0
        s = set(deadends)
        if '0000' in s:
            return -1
        q = deque([('0000', 0)])
        s.add('0000')
        while q:
            p, turns = q.popleft()
            for t in next(p):
                if t == target:
                    return turns + 1
                if t not in s:
                    q.append((t, turns + 1))
                    s.add(t)
        return -1

def openLock(deadends: List[str], target: str) -> int:
    return Solution().openLock(deadends, target)