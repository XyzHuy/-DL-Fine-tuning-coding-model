import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Initialize the count of columns to delete
        delete_count = 0
        
        # Get the number of columns (length of each string)
        num_columns = len(strs[0])
        
        # Iterate over each column
        for col in range(num_columns):
            # Check if the current column is sorted
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    delete_count += 1
                    break
        
        return delete_count

def minDeletionSize(strs: List[str]) -> int:
    return Solution().minDeletionSize(strs)