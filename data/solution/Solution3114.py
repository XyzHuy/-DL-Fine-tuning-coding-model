import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findLatestTime(self, s: str) -> str:
        for h in range(11, -1, -1):
            for m in range(59, -1, -1):
                t = f"{h:02d}:{m:02d}"
                if all(a == b for a, b in zip(s, t) if a != "?"):
                    return t

def findLatestTime(s: str) -> str:
    return Solution().findLatestTime(s)