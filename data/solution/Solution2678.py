import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            age = int(detail[11:13])  # Extract the age from the string
            if age > 60:
                count += 1
        return count

def countSeniors(details: List[str]) -> int:
    return Solution().countSeniors(details)