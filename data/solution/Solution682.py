import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for op in operations:
            if op == '+':
                # Record a new score that is the sum of the previous two scores
                record.append(record[-1] + record[-2])
            elif op == 'D':
                # Record a new score that is the double of the previous score
                record.append(2 * record[-1])
            elif op == 'C':
                # Invalidate and remove the previous score
                record.pop()
            else:
                # Record a new score of x
                record.append(int(op))
        
        return sum(record)

def calPoints(operations: List[str]) -> int:
    return Solution().calPoints(operations)