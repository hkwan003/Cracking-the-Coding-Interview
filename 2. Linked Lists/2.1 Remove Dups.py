class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def output(self):
        node = self
        while node is not None:
            print(node.val)
            node = node.next

    def removeDuplicates(self):
        hashTable = {}
        previous = Node(None)
        node = self
        while node is not None:
            if node.val in hashTable:
                previous.next = node.next
            else:
                hashTable[node.val] = node.val
                previous = node
            node = node.next



node1 = Node(1)
node2 = Node(1)
node3 = Node(2)
node4 = Node(3)
node5 = Node(4)
node6 = Node(5)
node7 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

node1.removeDuplicates()
print("\n")
node1.output()

