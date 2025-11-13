def toHex(num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
        return '0'
    # letter map
    mp = '0123456789abcdef'
    ans = ''
    for _ in range(8):
        # get last 4 digits
        # num & 1111b
        n = num & 15
        # hex letter for current 1111
        c = mp[n]
        ans = c + ans
        # num = num / 16
        num = num >> 4
    #strip leading zeroes
    return ans.lstrip('0')
