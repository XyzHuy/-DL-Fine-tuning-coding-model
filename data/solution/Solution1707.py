import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Step 1: Sort nums
        nums.sort()
        
        # Step 2: Sort queries by the second element (mi) and keep track of original indices
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        
        # Step 3: Initialize the Trie
        trie = {}
        
        # Helper function to add a number to the Trie
        def add_to_trie(num):
            node = trie
            for i in range(31, -1, -1):  # Assuming numbers are up to 10^9, which fits in 30 bits
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
        
        # Helper function to find the maximum XOR of xi with any number in the Trie
        def max_xor(xi):
            node = trie
            if not node:
                return -1
            max_xor_value = 0
            for i in range(31, -1, -1):
                bit = (xi >> i) & 1
                opposite_bit = 1 - bit
                if opposite_bit in node:
                    max_xor_value |= (1 << i)
                    node = node[opposite_bit]
                else:
                    node = node[bit]
            return max_xor_value
        
        # Step 4: Process each query
        results = [-1] * len(queries)
        nums_index = 0
        for original_index, (xi, mi) in sorted_queries:
            # Add all numbers <= mi to the Trie
            while nums_index < len(nums) and nums[nums_index] <= mi:
                add_to_trie(nums[nums_index])
                nums_index += 1
            # Find the maximum XOR for xi
            results[original_index] = max_xor(xi)
        
        # Step 5: Return the results
        return results

def maximizeXor(nums: List[int], queries: List[List[int]]) -> List[int]:
    return Solution().maximizeXor(nums, queries)