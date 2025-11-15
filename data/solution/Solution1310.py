import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Create a prefix XOR array
        prefix_xor = [0] * len(arr)
        prefix_xor[0] = arr[0]
        for i in range(1, len(arr)):
            prefix_xor[i] = prefix_xor[i-1] ^ arr[i]
        
        # Process each query
        answer = []
        for left, right in queries:
            if left == 0:
                answer.append(prefix_xor[right])
            else:
                answer.append(prefix_xor[right] ^ prefix_xor[left-1])
        
        return answer

def xorQueries(arr: List[int], queries: List[List[int]]) -> List[int]:
    return Solution().xorQueries(arr, queries)