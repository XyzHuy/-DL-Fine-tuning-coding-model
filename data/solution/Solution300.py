import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # This list will store the smallest tail of all increasing subsequences
        # with different lengths found so far.
        tails = []
        
        for num in nums:
            # Use binary search to find the insertion point of the current number
            # in the tails list.
            index = bisect.bisect_left(tails, num)
            
            # If the number is larger than any element in tails, append it.
            if index == len(tails):
                tails.append(num)
            else:
                # Otherwise, replace the element at the found index with the current number.
                tails[index] = num
        
        # The length of the tails list is the length of the longest increasing subsequence.
        return len(tails)

# Example usage:
# solution = Solution()
# print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))  # Output: 4
# print(solution.lengthOfLIS([0,1,0,3,2,3]))         # Output: 4
# print(solution.lengthOfLIS([7,7,7,7,7,7,7]))        # Output: 1

def lengthOfLIS(nums: List[int]) -> int:
    return Solution().lengthOfLIS(nums)