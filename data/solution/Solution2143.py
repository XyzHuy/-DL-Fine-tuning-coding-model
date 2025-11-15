import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

MOD = 10**9 + 7

class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        total_count = 0
        
        # Dictionary to store the count of differences
        dp = defaultdict(int)
        
        for i in range(n):
            new_dp = defaultdict(int)
            
            # If we pick nums1[i]
            new_dp[nums1[i]] += 1
            new_dp[nums1[i]] %= MOD
            
            # If we pick nums2[i]
            new_dp[-nums2[i]] += 1
            new_dp[-nums2[i]] %= MOD
            
            # Update the new_dp based on previous differences
            for diff, count in dp.items():
                # If we pick nums1[i] after some previous picks
                new_dp[diff + nums1[i]] += count
                new_dp[diff + nums1[i]] %= MOD
                
                # If we pick nums2[i] after some previous picks
                new_dp[diff - nums2[i]] += count
                new_dp[diff - nums2[i]] %= MOD
            
            # Add the count of balanced ranges ending at i
            total_count += new_dp[0]
            total_count %= MOD
            
            # Update dp for the next iteration
            dp = new_dp
        
        return total_count

def countSubranges(nums1: List[int], nums2: List[int]) -> int:
    return Solution().countSubranges(nums1, nums2)