def canWin(s):
    if s is None or len(s) < 2:
        return False
    list_s = list(s)
    return canWin_helper(list_s)

def canWin_helper(s):
    for i in range(len(s) - 1):
        if s[i] == '+' and s[i + 1] == '+':
            s[i] = '-'
            s[i + 1] = '-'
            res = canWin_helper(s)
            s[i] = '+'
            s[i + 1] = '+'
            if not res:
                return True
    return False