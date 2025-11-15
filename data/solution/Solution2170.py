import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        # Count frequencies of numbers at even and odd indices
        even_count = Counter(nums[::2])
        odd_count = Counter(nums[1::2])
        
        # Get the most common elements
        even_most_common = even_count.most_common(2)
        odd_most_common = odd_count.most_common(2)
        
        # If there's only one unique number at even or odd indices
        if len(even_most_common) == 1:
            even_most_common.append((0, 0))  # Append a dummy (number, count) pair
        if len(odd_most_common) == 1:
            odd_most_common.append((0, 0))  # Append a dummy (number, count) pair
        
        # Unpack the most common elements
        even_first_num, even_first_count = even_most_common[0]
        even_second_num, even_second_count = even_most_common[1]
        odd_first_num, odd_first_count = odd_most_common[0]
        odd_second_num, odd_second_count = odd_most_common[1]
        
        # If the most frequent numbers at even and odd indices are different
        if even_first_num != odd_first_num:
            return len(nums) - even_first_count - odd_first_count
        else:
            # If they are the same, we need to choose the best combination
            return len(nums) - max(even_first_count + odd_second_count, even_second_count + odd_first_count)

# Example usage:
# sol = Solution()
# print(sol.minimumOperations([3,1,3,2,4,3]))  # Output: 3
# print(sol.minimumOperations([1,2,2,2,2]))    # Output: 2

def minimumOperations(nums: List[int]) -> int:
    return Solution().minimumOperations(nums)