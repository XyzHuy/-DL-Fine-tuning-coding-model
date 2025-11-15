import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Calculate the wealth of each customer by summing their bank accounts
        customer_wealths = [sum(customer_accounts) for customer_accounts in accounts]
        # Return the maximum wealth found
        return max(customer_wealths)

def maximumWealth(accounts: List[List[int]]) -> int:
    return Solution().maximumWealth(accounts)