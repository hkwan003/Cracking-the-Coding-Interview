class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def removeKthToLast(self, n):
        if n < 0:
            return
        counter = 0
        node = self
        while node is not None:
            counter += 1
            node = node.next
        if n > counter:
            print("Sorry your input was incorrect")
            return
        counter -= n
        node = self
        while node is not None:
            counter -= 1
            if counter == 0:
                print(node.val)
            node = node.next



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

node1.removeKthToLast(9)
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7


