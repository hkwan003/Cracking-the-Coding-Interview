def StringRotation(strInput1, strInput2):
    if len(strInput1) != len(strInput2):
        return False
    for i in range(len(strInput1)):
        temp = strInput1[i:] + strInput1[:i]
        if temp == strInput2:
            return True
    return False



print(StringRotation("waterbottle", "erbottlewat"))