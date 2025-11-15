import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the current window of 1's
        # and the previous window of 1's
        prev_length = 0
        current_length = 0
        max_length = 0
        zero_found = False

        for num in nums:
            if num == 1:
                # If the number is 1, increase the current window length
                current_length += 1
            else:
                # If the number is 0, update the max length if necessary
                # and reset the current window length
                if zero_found:
                    max_length = max(max_length, prev_length + current_length)
                    prev_length = current_length
                else:
                    # If no zero has been found yet, we can consider
                    # the current length as the previous length
                    prev_length = current_length
                    zero_found = True
                current_length = 0

        # If the array ends with a sequence of 1's, we need to update the max length
        if zero_found:
            max_length = max(max_length, prev_length + current_length)
        else:
            # If no zero was found, we must delete one element, so we return len(nums) - 1
            return len(nums) - 1

        return max_length

def longestSubarray(nums: List[int]) -> int:
    return Solution().longestSubarray(nums)