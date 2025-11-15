import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        # Create a prefix XOR matrix of the same size
        prefix_xor = [[0] * n for _ in range(m)]
        max_heap = []
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    prefix_xor[i][j] = matrix[i][j]
                elif i == 0:
                    prefix_xor[i][j] = prefix_xor[i][j - 1] ^ matrix[i][j]
                elif j == 0:
                    prefix_xor[i][j] = prefix_xor[i - 1][j] ^ matrix[i][j]
                else:
                    prefix_xor[i][j] = prefix_xor[i - 1][j] ^ prefix_xor[i][j - 1] ^ prefix_xor[i - 1][j - 1] ^ matrix[i][j]
                
                # Use a min-heap to keep track of the k largest elements
                heapq.heappush(max_heap, prefix_xor[i][j])
                if len(max_heap) > k:
                    heapq.heappop(max_heap)
        
        # The root of the heap is the kth largest element
        return max_heap[0]

def kthLargestValue(matrix: List[List[int]], k: int) -> int:
    return Solution().kthLargestValue(matrix, k)