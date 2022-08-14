# https://leetcode.com/problems/linked-list-cycle/discuss/1829489/C%2B%2B-oror-Easy-To-Understand-oror-2-Pointer-oror-Fast-and-Slow


def hasCycle(head):

    slow = fast = head

    if not head:
        return False

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
