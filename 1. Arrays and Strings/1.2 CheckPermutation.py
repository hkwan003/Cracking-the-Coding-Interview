def CheckPermutation(str1, str2):
    return sorted(str1) == sorted(str2)

print(CheckPermutation("abc", "cbaa"))