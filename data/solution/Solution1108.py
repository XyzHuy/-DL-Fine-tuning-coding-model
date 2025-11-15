import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

def defangIPaddr(address: str) -> str:
    return Solution().defangIPaddr(address)