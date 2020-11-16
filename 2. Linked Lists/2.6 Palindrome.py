class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def palindrome(self):
        stack = []
        node = self

        while node is not None:
            if node.val not in stack:
                stack.append(node.val)
            else:
                if len(stack) != 0 and stack[-1] == node.val:
                    stack.pop()
            node = node.next
        print(len(stack) == 0)



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(1)
node5 = Node(2)
node6 = Node(1)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

node1.palindrome()




