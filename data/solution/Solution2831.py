import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        max_length = 0
        most_frequent = 0
        
        for right in range(len(nums)):
            num = nums[right]
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            
            most_frequent = max(most_frequent, freq[num])
            
            # Calculate the current window size
            window_size = right - left + 1
            
            # Calculate the number of deletions needed
            deletions_needed = window_size - most_frequent
            
            # If deletions needed exceed k, shrink the window from the left
            if deletions_needed > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            
            # Update the maximum length of the equal subarray
            max_length = max(max_length, window_size - deletions_needed)
        
        return max_length

# Example usage:
# sol = Solution()
# print(sol.longestEqualSubarray([1,3,2,3,1,3], 3))  # Output: 3
# print(sol.longestEqualSubarray([1,1,2,2,1,1], 2))  # Output: 4

def longestEqualSubarray(nums: List[int], k: int) -> int:
    return Solution().longestEqualSubarray(nums, k)