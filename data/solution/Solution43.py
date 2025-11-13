def multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    res = ''
    ls1, ls2, = len(num1), len(num2)
    ls = ls1 + ls2
    # list stores int
    arr = [0] * ls
    for i in reversed(range(ls1)):
        for j in reversed(range(ls2)):
            # store the direct results of multiply two ints
            arr[i + j + 1] += int(num1[i]) * int(num2[j])
    for i in reversed(range(1, ls)):
        # digital plus
        arr[i - 1] += arr[i] / 10
        arr[i] %= 10
    pos = 0
    # to string
    if arr[pos] == 0:
        pos += 1
    while pos < ls:
        res = res + str(arr[pos])
        pos += 1
    return res
