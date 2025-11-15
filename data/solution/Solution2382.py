import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        parent = list(range(n))
        size = [0] * n
        max_sum = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] < size[rootY]:
                    rootX, rootY = rootY, rootX
                parent[rootY] = rootX
                size[rootX] += size[rootY]
                max_sum[rootX] += max_sum[rootY]
                max_sum[rootY] = 0

        result = [0] * n
        current_max = 0

        for i in range(n - 1, 0, -1):
            index = removeQueries[i]
            size[index] = nums[index]
            max_sum[index] = nums[index]
            current_max = max(current_max, max_sum[index])

            if index - 1 >= 0 and size[index - 1] > 0:
                union(index, index - 1)
                current_max = max(current_max, max_sum[find(index)])

            if index + 1 < n and size[index + 1] > 0:
                union(index, index + 1)
                current_max = max(current_max, max_sum[find(index)])

            result[i - 1] = current_max

        return result

def maximumSegmentSum(nums: List[int], removeQueries: List[int]) -> List[int]:
    return Solution().maximumSegmentSum(nums, removeQueries)