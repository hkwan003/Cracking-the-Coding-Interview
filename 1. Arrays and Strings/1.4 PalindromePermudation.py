import collections

def PalindromePermutation(input):
    input = input.replace(' ', '')
    input = input.lower()
    hashTable = collections.defaultdict(lambda: 0)
    for i in input:
        hashTable[i] += 1

    oddCount = 0
    for i, j in hashTable.items():
        if j % 2 != 0 and oddCount == 0:
            oddCount += 1
        elif j % 2 != 0 and oddCount != 0:
            return False
    return True

print(PalindromePermutation("Tact Coa"))