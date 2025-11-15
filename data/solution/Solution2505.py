import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        cnt = [0] * 64
        ans = 0
        for v in nums:
            for i in range(31):
                if (v >> i) & 1:
                    cnt[i] += 1
        for i in range(63):
            if cnt[i]:
                ans |= 1 << i
            cnt[i + 1] += cnt[i] // 2
        return ans

def subsequenceSumOr(nums: List[int]) -> int:
    return Solution().subsequenceSumOr(nums)