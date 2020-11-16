def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None or head.next == None:
        return None

    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            curr = head
            while curr != fast:
                fast = fast.next
                curr = curr.next
                print(curr.val, fast.val)
            return curr