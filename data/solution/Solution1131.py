import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        max_val = 0
        
        # We consider the expression |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
        # This can be broken down into 8 possible cases based on the combinations of signs
        # We will compute the maximum and minimum values for each case and find the difference
        
        # Case 1: arr1[i] + arr2[i] + i and arr1[j] + arr2[j] + j
        max1 = max(arr1[i] + arr2[i] + i for i in range(n))
        min1 = min(arr1[i] + arr2[i] + i for i in range(n))
        max_val = max(max_val, max1 - min1)
        
        # Case 2: arr1[i] + arr2[i] - i and arr1[j] + arr2[j] - j
        max2 = max(arr1[i] + arr2[i] - i for i in range(n))
        min2 = min(arr1[i] + arr2[i] - i for i in range(n))
        max_val = max(max_val, max2 - min2)
        
        # Case 3: arr1[i] - arr2[i] + i and arr1[j] - arr2[j] + j
        max3 = max(arr1[i] - arr2[i] + i for i in range(n))
        min3 = min(arr1[i] - arr2[i] + i for i in range(n))
        max_val = max(max_val, max3 - min3)
        
        # Case 4: arr1[i] - arr2[i] - i and arr1[j] - arr2[j] - j
        max4 = max(arr1[i] - arr2[i] - i for i in range(n))
        min4 = min(arr1[i] - arr2[i] - i for i in range(n))
        max_val = max(max_val, max4 - min4)
        
        # Case 5: -arr1[i] + arr2[i] + i and -arr1[j] + arr2[j] + j
        max5 = max(-arr1[i] + arr2[i] + i for i in range(n))
        min5 = min(-arr1[i] + arr2[i] + i for i in range(n))
        max_val = max(max_val, max5 - min5)
        
        # Case 6: -arr1[i] + arr2[i] - i and -arr1[j] + arr2[j] - j
        max6 = max(-arr1[i] + arr2[i] - i for i in range(n))
        min6 = min(-arr1[i] + arr2[i] - i for i in range(n))
        max_val = max(max_val, max6 - min6)
        
        # Case 7: -arr1[i] - arr2[i] + i and -arr1[j] - arr2[j] + j
        max7 = max(-arr1[i] - arr2[i] + i for i in range(n))
        min7 = min(-arr1[i] - arr2[i] + i for i in range(n))
        max_val = max(max_val, max7 - min7)
        
        # Case 8: -arr1[i] - arr2[i] - i and -arr1[j] - arr2[j] - j
        max8 = max(-arr1[i] - arr2[i] - i for i in range(n))
        min8 = min(-arr1[i] - arr2[i] - i for i in range(n))
        max_val = max(max_val, max8 - min8)
        
        return max_val

def maxAbsValExpr(arr1: List[int], arr2: List[int]) -> int:
    return Solution().maxAbsValExpr(arr1, arr2)