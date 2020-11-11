def oneAway(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if abs(len1 - len2) > 1:
        return False

    if len1 == len2:
        return sameLength(str1, str2, len1)
    if len1 + 1 == len2:
        return oneEditInsert(str1, str2)
    if len1 == 1 + len2:
        return oneEditInsert(str2, str1)


def sameLength(str1, str2, length):
    count = 0
    for i in range(length):
        if str1[i] != str2[i]:
            count += 1
    return count == 1

def oneEditInsert(str1, str2):
    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(str1) and ptr2 < len(str2):
        if str1[ptr1] != str2[ptr2]:
            if ptr1 != ptr2:
                return False
            else:
                ptr2 += 1
        else:
            ptr1 += 1
            ptr2 += 1
    return True

print(oneAway("ple", "pales"))
