import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapper = defaultdict(set)
        for i, num in enumerate(nums2):
            mapper[num].add(i)
        return [mapper[num].pop() for num in nums1]

def anagramMappings(nums1: List[int], nums2: List[int]) -> List[int]:
    return Solution().anagramMappings(nums1, nums2)