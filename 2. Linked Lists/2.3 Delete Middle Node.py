class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def output(self):
        node = self
        while node is not None:
            print(node.val)
            node = node.next

    def deleteMiddleNode(self, n):
        node = self
        previous = Node(0)
        while node is not None:
            if n == node.val and node.next is not None:
                previous.next = node.next
            else:
                previous = node
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

node1.deleteMiddleNode(4)
node1.output()


