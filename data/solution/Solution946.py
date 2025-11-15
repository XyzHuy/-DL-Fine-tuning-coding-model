import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack

def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    return Solution().validateStackSequences(pushed, popped)