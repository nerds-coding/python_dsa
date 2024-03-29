# https://leetcode.com/problems/copy-list-with-random-pointer/


def copyRandomList(head):
    if not head:
        return
    # copy nodes
    cur = head
    while cur:
        nxt = cur.next
        cur.next = Node(cur.val)
        cur.next.next = nxt
        cur = nxt

    # copy random pointers
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next

    # separate two parts
    second = cur = head.next
    while cur.next:
        head.next = cur.next  # here we are directly
        # using the head which is unused till now
        head = head.next
        cur.next = head.next
        cur = cur.next

    head.next = None

    return second
