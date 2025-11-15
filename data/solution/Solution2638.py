import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        # Create a set for O(1) lookups
        num_set = set(nums)
        
        # Dictionary to hold chains of numbers that are k apart
        chains = defaultdict(list)
        
        # Find all chains
        for num in nums:
            if num not in num_set:
                continue
            # Find the chain for this number going upwards
            chain = []
            current = num
            while current in num_set:
                chain.append(current)
                num_set.remove(current)
                current += k
            
            # Find the chain for this number going downwards
            current = num - k
            while current in num_set:
                chain.append(current)
                num_set.remove(current)
                current -= k
            
            # Sort the chain and add to chains dictionary
            chain.sort()
            chains[len(chain)].append(chain)
        
        # Function to count k-free subsets for a chain of length n
        def count_subsets(n):
            if n == 0:
                return 1
            if n == 1:
                return 2
            dp = [0] * (n + 1)
            dp[0] = 1  # The empty subset
            dp[1] = 2  # The empty subset and the single element subset
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
            return dp[n]
        
        # Calculate the total number of k-free subsets
        total_subsets = 1
        for chain_length in chains:
            for _ in chains[chain_length]:
                total_subsets *= count_subsets(chain_length)
        
        return total_subsets

def countTheNumOfKFreeSubsets(nums: List[int], k: int) -> int:
    return Solution().countTheNumOfKFreeSubsets(nums, k)