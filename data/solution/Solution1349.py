import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        
        # Convert each row to a bitmask
        def to_mask(row):
            mask = 0
            for seat in row:
                mask = (mask << 1) | (1 if seat == '#' else 0)
            return mask
        
        # Generate all possible valid masks for a row
        def generate_valid_masks():
            valid_masks = []
            for mask in range(1 << n):
                if (mask & (mask >> 1)) == 0:  # No two students adjacent
                    valid_masks.append(mask)
            return valid_masks
        
        # Check if mask1 can be placed below mask2 without cheating
        def is_valid(mask1, mask2):
            return (mask1 & (mask2 >> 1)) == 0 and (mask1 & (mask2 << 1)) == 0
        
        # Convert rows to bitmasks
        row_masks = [to_mask(row) for row in seats]
        valid_masks = generate_valid_masks()
        
        # Initialize dp table
        dp = [[-1] * (1 << n) for _ in range(m)]
        
        # Fill the first row of dp table
        for mask in valid_masks:
            if (mask & row_masks[0]) == 0:  # No broken seats in this arrangement
                dp[0][mask] = bin(mask).count('1')
        
        # Fill the rest of the dp table
        for r in range(1, m):
            for mask1 in valid_masks:
                if (mask1 & row_masks[r]) == 0:  # No broken seats in this arrangement
                    for mask2 in valid_masks:
                        if is_valid(mask1, mask2):
                            dp[r][mask1] = max(dp[r][mask1], dp[r-1][mask2] + bin(mask1).count('1'))
        
        # The answer is the maximum value in the last row of dp table
        return max(dp[-1])

# Example usage:
# sol = Solution()
# print(sol.maxStudents([["#",".","#","#",".","#"],
#                        [".","#","#","#","#","."],
#                        ["#",".","#","#",".","#"]]))  # Output: 4

def maxStudents(seats: List[List[str]]) -> int:
    return Solution().maxStudents(seats)