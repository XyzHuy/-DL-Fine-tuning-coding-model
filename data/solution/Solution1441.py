import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        stack = []
        stream_index = 1
        
        for number in target:
            while stream_index < number:
                operations.append("Push")
                operations.append("Pop")
                stream_index += 1
            
            operations.append("Push")
            stack.append(stream_index)
            stream_index += 1
        
        return operations

def buildArray(target: List[int], n: int) -> List[str]:
    return Solution().buildArray(target, n)