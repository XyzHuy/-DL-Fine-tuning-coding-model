def generateParenthesis(n):
    if n == 1:
        return ['()']
    last_list = generateParenthesis(n - 1)
    res = []
    for t in last_list:
        curr = t + ')'
        for index in range(len(curr)):
            if curr[index] == ')':
                res.append(curr[:index] + '(' + curr[index:])
    return list(set(res))
