import random
import functools
import collections
import string
import math
import datetime


from typing import List

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.tree[idx] += val
            idx += idx & -idx
    
    def query(self, idx):
        idx += 1
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & -idx
        return result

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        # Create a mapping from value to its index in nums1
        pos1 = {x: i for i, x in enumerate(nums1)}
        
        # Create a compressed array based on the positions in nums1
        compressed = [pos1[x] for x in nums2]
        
        # BIT for counting elements less than current index
        bit_less = BIT(n)
        # BIT for counting elements greater than current index
        bit_greater = BIT(n)
        
        # Initialize bit_greater with all elements
        for i in range(n):
            bit_greater.update(compressed[i], 1)
        
        good_triplets = 0
        
        for i in range(n):
            val = compressed[i]
            # Decrease the count of this value in bit_greater
            bit_greater.update(val, -1)
            
            # Count of elements less than val in bit_less
            count_less = bit_less.query(val - 1)
            # Count of elements greater than val in bit_greater
            count_greater = bit_greater.query(n - 1) - bit_greater.query(val)
            
            # Number of good triplets with val as the middle element
            good_triplets += count_less * count_greater
            
            # Update bit_less with this value
            bit_less.update(val, 1)
        
        return good_triplets

def goodTriplets(nums1: List[int], nums2: List[int]) -> int:
    return Solution().goodTriplets(nums1, nums2)