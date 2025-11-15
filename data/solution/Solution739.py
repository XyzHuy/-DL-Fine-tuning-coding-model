import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        
        return answer

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    return Solution().dailyTemperatures(temperatures)