import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        def count_triplets(nums1, nums2):
            count = 0
            n2_product_count = defaultdict(int)
            
            # Count all possible products of pairs in nums2
            for j in range(len(nums2)):
                for k in range(j + 1, len(nums2)):
                    n2_product_count[nums2[j] * nums2[k]] += 1
            
            # Check for each num1[i]^2 if it exists in the product count of nums2
            for num in nums1:
                target = num * num
                count += n2_product_count[target]
            
            return count
        
        # Count type 1 triplets and type 2 triplets
        type1 = count_triplets(nums1, nums2)
        type2 = count_triplets(nums2, nums1)
        
        return type1 + type2

def numTriplets(nums1: List[int], nums2: List[int]) -> int:
    return Solution().numTriplets(nums1, nums2)