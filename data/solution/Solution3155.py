import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        answer = []
        
        for i in range(len(count)):
            max_upgrades = 0
            for j in range(count[i] + 1):
                # Money after selling j servers
                total_money = money[i] + j * sell[i]
                # Servers left to potentially upgrade
                servers_left = count[i] - j
                # Calculate the number of servers we can upgrade with the available money
                possible_upgrades = total_money // upgrade[i]
                # The actual number of servers we can upgrade is the minimum of servers_left and possible_upgrades
                actual_upgrades = min(servers_left, possible_upgrades)
                # Update the maximum number of upgrades
                max_upgrades = max(max_upgrades, actual_upgrades)
            
            answer.append(max_upgrades)
        
        return answer

def maxUpgrades(count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
    return Solution().maxUpgrades(count, upgrade, sell, money)