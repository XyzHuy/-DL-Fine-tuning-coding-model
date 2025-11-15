import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            unique_emails.add(local + '@' + domain)
        
        return len(unique_emails)

def numUniqueEmails(emails: List[str]) -> int:
    return Solution().numUniqueEmails(emails)