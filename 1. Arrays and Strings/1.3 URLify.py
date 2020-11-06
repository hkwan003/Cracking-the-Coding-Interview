def URLify(input):
    strArr = list(input)
    for i, c in enumerate(strArr):
        if c == ' ':
            strArr[i] = '%20'
    return ''.join(strArr)

print(URLify("Mr John Smith"))