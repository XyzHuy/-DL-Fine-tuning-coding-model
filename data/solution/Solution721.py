import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_id = {}
        
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_to_id:
                    uf.union(i, email_to_id[email])
                else:
                    email_to_id[email] = i
        
        merged_emails = defaultdict(set)
        for i, (_, *emails) in enumerate(accounts):
            root = uf.find(i)
            merged_emails[root].update(emails)
        
        return [[accounts[root][0]] + sorted(emails) for root, emails in merged_emails.items()]

def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    return Solution().accountsMerge(accounts)