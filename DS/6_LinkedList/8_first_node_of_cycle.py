# http://hrishikeshmishra.com/how-to-find-the-starting-point-of-a-loop-in-a-linked-list/


def find_first_node_of_cycle(head):
    slow = fast = head

    isCycle = False
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            isCycle = True
            break

    if not isCycle:
        return None

    while head != slow:
        slow, head = slow.next, head.next

    return slow

