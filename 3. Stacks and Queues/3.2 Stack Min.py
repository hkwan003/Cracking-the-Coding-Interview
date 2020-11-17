class minStack:
    def __init__(self):
        self.s = []
        self.minVal = float("inf")

    def push(self, x):
        self.s.append(x)
        if x < self.minVal:
            self.minVal = x

    def updateMin(self):
        newMin = float("inf")
        for item in self.s:
            if item < newMin:
                newMin = item
        self.minVal = newMin

    def pop(self):
        item = self.s.pop()
        if item == self.minVal:
            self.updateMin()
        return item

    def top(self):
        return self.s[-1]

    def getMin(self):
        return self.minVal

if __name__ == "__main__":
    minimum = minStack()
    minimum.push(5)
    minimum.push(1)
    print(minimum.getMin())
    print(minimum.pop())
    print(minimum.getMin())