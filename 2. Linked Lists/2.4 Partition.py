class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def output(self):
        node = self
        while node is not None:
            print(node.val)
            node = node.next

    def partition(self, x):
        headPtr = beforeHead = Node(0)
        tailPtr = afterHead = Node(0)
        node = self
        while node is not None:
            if node.val < x:
                headPtr.next = node
                headPtr = headPtr.next
            else:
                tailPtr.next = node
                tailPtr = tailPtr.next
            node = node.next

        tailPtr.next = None
        headPtr.next = afterHead.next

        while beforeHead is not None:
            print(beforeHead.val)
            beforeHead = beforeHead.next
        #This output prints out an additional zero due to linkedList initalization


node1 = Node(3)
node2 = Node(5)
node3 = Node(8)
node4 = Node(5)
node5 = Node(10)
node6 = Node(2)
node7 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

node1.partition(5)

