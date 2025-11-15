import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def interpret(self, command: str) -> str:
        # Replace '()' with 'o' and '(al)' with 'al'
        return command.replace('()', 'o').replace('(al)', 'al')

def interpret(command: str) -> str:
    return Solution().interpret(command)