import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for operation in operations:
            if operation == "++X" or operation == "X++":
                X += 1
            elif operation == "--X" or operation == "X--":
                X -= 1
        return X

def finalValueAfterOperations(operations: List[str]) -> int:
    return Solution().finalValueAfterOperations(operations)