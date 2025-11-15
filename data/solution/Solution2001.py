import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_count = defaultdict(int)
        for width, height in rectangles:
            ratio = width / height
            ratio_count[ratio] += 1
        
        interchangeable_pairs = 0
        for count in ratio_count.values():
            if count > 1:
                interchangeable_pairs += (count * (count - 1)) // 2
        
        return interchangeable_pairs

def interchangeableRectangles(rectangles: List[List[int]]) -> int:
    return Solution().interchangeableRectangles(rectangles)