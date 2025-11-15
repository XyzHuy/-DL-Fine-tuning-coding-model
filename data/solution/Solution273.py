import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        billion = 10 ** 9
        million = 10 ** 6
        thousand = 10 ** 3
        hundred = 10 ** 2
        
        below_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_twenty[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return below_twenty[n // 100] + " Hundred " + helper(n % 100)
        
        result = ""
        
        if num >= billion:
            result += helper(num // billion) + "Billion "
            num %= billion
        if num >= million:
            result += helper(num // million) + "Million "
            num %= million
        if num >= thousand:
            result += helper(num // thousand) + "Thousand "
            num %= thousand
        if num > 0:
            result += helper(num)
        
        return result.strip()

def numberToWords(num: int) -> str:
    return Solution().numberToWords(num)