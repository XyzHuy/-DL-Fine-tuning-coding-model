import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # Step 1: Map each element in target to its index
        index_map = {num: idx for idx, num in enumerate(target)}
        
        # Step 2: Transform arr into a sequence of indices based on target
        transformed_arr = [index_map[num] for num in arr if num in index_map]
        
        # Step 3: Find the LIS in the transformed array
        def length_of_lis(sequence):
            # This function finds the length of the LIS using binary search
            lis = []
            for num in sequence:
                pos = binary_search(lis, num)
                if pos == len(lis):
                    lis.append(num)
                else:
                    lis[pos] = num
            return len(lis)
        
        def binary_search(lis, num):
            left, right = 0, len(lis)
            while left < right:
                mid = (left + right) // 2
                if lis[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        lis_length = length_of_lis(transformed_arr)
        
        # Step 4: Calculate the minimum number of insertions
        return len(target) - lis_length

def minOperations(target: List[int], arr: List[int]) -> int:
    return Solution().minOperations(target, arr)