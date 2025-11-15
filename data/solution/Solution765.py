import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        # Create unions for couples
        for i in range(0, len(row), 2):
            # Each couple is represented by the smaller number divided by 2
            union(row[i] // 2, row[i + 1] // 2)
        
        # Count the number of unique roots (connected components)
        unique_roots = set(find(i) for i in range(n))
        
        # The minimum number of swaps is the number of connected components - 1
        return n - len(unique_roots)

# Example usage:
# sol = Solution()
# print(sol.minSwapsCouples([0,2,1,3]))  # Output: 1
# print(sol.minSwapsCouples([3,2,0,1]))  # Output: 0

def minSwapsCouples(row: List[int]) -> int:
    return Solution().minSwapsCouples(row)