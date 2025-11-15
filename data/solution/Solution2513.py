import random
import functools
import collections
import string
import math
import datetime


import math

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def can_form_sets(mid):
            lcm = (divisor1 * divisor2) // math.gcd(divisor1, divisor2)
            not_div_by_divisor1 = mid - mid // divisor1
            not_div_by_divisor2 = mid - mid // divisor2
            not_div_by_both = mid - mid // lcm
            
            # Check if we can form the sets
            return (not_div_by_divisor1 >= uniqueCnt1 and
                    not_div_by_divisor2 >= uniqueCnt2 and
                    not_div_by_both >= uniqueCnt1 + uniqueCnt2)
        
        left, right = 1, 10**10
        while left < right:
            mid = (left + right) // 2
            if can_form_sets(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

def minimizeSet(divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
    return Solution().minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2)