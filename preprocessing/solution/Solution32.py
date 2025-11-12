def longestValidParentheses(s):
    
    ls = len(s)
    stack = []
    data = [0] * ls
    for i in range(ls):
        curr = s[i]
        if curr == '(':
            stack.append(i)
        else:
            if len(stack) > 0:
                data[i] = 1
                data[stack.pop(-1)] = 1
    tep, res = 0, 0
    for t in data:
        if t == 1:
            tep += 1
        else:
            res = max(tep, res)
            tep = 0
    return max(tep, res)
