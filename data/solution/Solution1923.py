import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        def check(l):
            mod = 10**11 + 7
            base = 31
            P = [1] * (max_len + 1)
            for i in range(1, max_len + 1):
                P[i] = (P[i - 1] * base) % mod

            def hash_value(seq):
                val = 0
                for x in seq:
                    val = (val * base + x + 1) % mod
                return val

            def get_hashes(seq):
                h = hash_value(seq[:l])
                hashes = {h}
                for i in range(l, len(seq)):
                    h = (h - (seq[i - l] + 1) * P[l - 1]) % mod
                    h = (h * base + seq[i] + 1) % mod
                    hashes.add(h)
                return hashes

            first_hashes = get_hashes(paths[0])
            for path in paths[1:]:
                if len(path) < l:
                    return False
                path_hashes = get_hashes(path)
                first_hashes.intersection_update(path_hashes)
                if not first_hashes:
                    return False
            return True

        max_len = min(len(p) for p in paths)
        left, right = 0, max_len
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left

def longestCommonSubpath(n: int, paths: List[List[int]]) -> int:
    return Solution().longestCommonSubpath(n, paths)