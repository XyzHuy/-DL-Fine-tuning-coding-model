import random
import functools
import collections
import string
import math
import datetime


from typing import List
from math import inf

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def dfs(i):
            if i >= len(cookies):
                nonlocal ans
                ans = min(ans, max(cnt))
                return
            for j in range(k):
                if cnt[j] + cookies[i] >= ans or (j > 0 and cnt[j] == cnt[j - 1]):
                    continue
                cnt[j] += cookies[i]
                dfs(i + 1)
                cnt[j] -= cookies[i]

        ans = inf
        cnt = [0] * k
        cookies.sort(reverse=True)
        dfs(0)
        return ans

def distributeCookies(cookies: List[int], k: int) -> int:
    return Solution().distributeCookies(cookies, k)