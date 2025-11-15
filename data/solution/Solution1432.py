import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        
        # To find the maximum number
        for i in range(len(num_str)):
            if num_str[i] != '9':
                max_num = int(num_str.replace(num_str[i], '9'))
                break
        else:
            max_num = num
        
        # To find the minimum number
        if num_str[0] != '1':
            min_num = int(num_str.replace(num_str[0], '1'))
        else:
            for i in range(1, len(num_str)):
                if num_str[i] not in ('0', '1'):
                    min_num = int(num_str.replace(num_str[i], '0'))
                    break
            else:
                min_num = num
        
        return max_num - min_num

def maxDiff(num: int) -> int:
    return Solution().maxDiff(num)