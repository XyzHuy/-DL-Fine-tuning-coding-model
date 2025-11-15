import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maximumTime(self, time: str) -> str:
        time_list = list(time)
        
        # Determine the first hour digit
        if time_list[0] == '?':
            if time_list[1] in ['4', '5', '6', '7', '8', '9']:
                time_list[0] = '1'
            else:
                time_list[0] = '2'
        
        # Determine the second hour digit
        if time_list[1] == '?':
            if time_list[0] == '2':
                time_list[1] = '3'
            else:
                time_list[1] = '9'
        
        # Determine the first minute digit
        if time_list[3] == '?':
            time_list[3] = '5'
        
        # Determine the second minute digit
        if time_list[4] == '?':
            time_list[4] = '9'
        
        return ''.join(time_list)

def maximumTime(time: str) -> str:
    return Solution().maximumTime(time)