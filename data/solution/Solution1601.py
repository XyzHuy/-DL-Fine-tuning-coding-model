import random
import functools
import collections
import string
import math
import datetime


from typing import List
from itertools import combinations

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def is_valid_request_set(request_set):
            balance = [0] * n
            for from_i, to_i in request_set:
                balance[from_i] -= 1
                balance[to_i] += 1
            return all(b == 0 for b in balance)
        
        max_requests = 0
        total_requests = len(requests)
        
        # Check all subsets of requests
        for k in range(total_requests, 0, -1):
            for request_set in combinations(requests, k):
                if is_valid_request_set(request_set):
                    return k
        return 0

def maximumRequests(n: int, requests: List[List[int]]) -> int:
    return Solution().maximumRequests(n, requests)