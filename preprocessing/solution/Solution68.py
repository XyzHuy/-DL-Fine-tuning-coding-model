def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    res = []
    res_list = []
    curr = []
    count, pos = 0, 0
    while pos < len(words):
        word = words[pos]
        if len(word) > maxWidth:
            pos += 1
        if len(word) + count + len(curr)<= maxWidth:
            count += len(word)
            curr.append(word)
            pos += 1
        else:
            res_list.append(curr)
            curr = []
            count = 0
    if len(curr) > 0:
        res_list.append(curr)
    # print res_list
    for index, curr in enumerate(res_list):
        text = ''
        remain = sum([len(t) for t in curr])
        if len(curr) == 1:
            # single word
            text = curr[0] + ' ' * (maxWidth - remain)
        elif index == len(res_list) - 1:
            # last line
            text = ' '.join(curr)
            text += ' ' * (maxWidth - remain - len(curr) + 1)
        else:
            # multiple
            step = (maxWidth - remain) / (len(curr) - 1 )
            extra = (maxWidth - remain) % (len(curr) - 1 )
            for index in range(len(curr) - 1):
                text += curr[index] + ' ' * step
                if extra > 0:
                    # assign from left
                    text += ' '
                    extra -= 1
            text += curr[-1]
        res.append(text)
    return res
