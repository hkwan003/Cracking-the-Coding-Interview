def stringCompression(inputStr):
    if len(inputStr) == 0:
        return
    previous = inputStr[0]
    count = 0
    result = ""

    for i in inputStr:
        if previous == i:
            count += 1
        else:
            result += previous + str(count)
            previous = i
            count = 1
    if count:
        result += previous + str(count)
    return result if len(result) <= len(inputStr) else inputStr

print(stringCompression("aa"))
# returnString = ""
# count = 1

# for i in range(len(inputStr) - 1):
#     if inputStr[i] == inputStr[i + 1]:
#         count += 1
#     else:
#         returnString += inputStr[i] + str(count)
#         count = 1
# returnString += inputStr[i + 1] + str(count)
#
# return returnString if len(returnString) < len(inputStr) else inputStr
