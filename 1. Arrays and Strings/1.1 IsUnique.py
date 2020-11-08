

def IsUnique(str):
    if len(str) > 128:
        return False

    sorted(str)
    for i in range(1, len(str)):
        if str[i] == str[i - 1]:
            return False
    return True
print(IsUnique("123456"))