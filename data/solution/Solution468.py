import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_valid_ipv4(ip):
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit():
                    return False
                if not 0 <= int(part) <= 255:
                    return False
                if part != str(int(part)):  # Check for leading zeros
                    return False
            return True

        def is_valid_ipv6(ip):
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            for part in parts:
                if not (1 <= len(part) <= 4):
                    return False
                if not all(c in '0123456789abcdefABCDEF' for c in part):
                    return False
            return True

        if '.' in queryIP:
            return "IPv4" if is_valid_ipv4(queryIP) else "Neither"
        elif ':' in queryIP:
            return "IPv6" if is_valid_ipv6(queryIP) else "Neither"
        else:
            return "Neither"

def validIPAddress(queryIP: str) -> str:
    return Solution().validIPAddress(queryIP)