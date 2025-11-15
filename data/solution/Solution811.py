import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            subdomains = domain.split('.')
            
            # Generate all subdomains
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                domain_count[subdomain] += count
        
        # Format the result as required
        result = [f"{count} {domain}" for domain, count in domain_count.items()]
        
        return result

def subdomainVisits(cpdomains: List[str]) -> List[str]:
    return Solution().subdomainVisits(cpdomains)