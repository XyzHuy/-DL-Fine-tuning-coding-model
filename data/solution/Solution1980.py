import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        # Create a bitmask where each bit at position i indicates if there is a binary string with i '1's in nums
        seen_ones_count = 0
        for binary in nums:
            # Count the number of '1's in the current binary string
            ones_count = binary.count("1")
            # Set the bit corresponding to this count in seen_ones_count
            seen_ones_count |= 1 << ones_count

        # Try to find a count of '1's that is not present in the nums
        for i in range(n + 1):
            if not (seen_ones_count >> i) & 1:
                # Construct a binary string with i '1's and (n - i) '0's
                return '1' * i + '0' * (n - i)

        # This line is theoretically unreachable because there are only n+1 possible counts of '1's (0 to n)
        # and we have n binary strings of length n, but it's good practice to return something
        return ""

# Example usage:
sol = Solution()
print(sol.findDifferentBinaryString(["01", "10"]))  # Output: "11" or "00"
print(sol.findDifferentBinaryString(["00", "01"]))  # Output: "11" or "10"
print(sol.findDifferentBinaryString(["111", "011", "001"]))  # Output: "101" or any other valid string

def findDifferentBinaryString(nums: List[str]) -> str:
    return Solution().findDifferentBinaryString(nums)