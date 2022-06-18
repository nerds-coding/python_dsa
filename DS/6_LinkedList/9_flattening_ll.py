# Problem statement

# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/


# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/150321/Easy-Understanding-Java-beat-95.7-with-Explanation
# iterative approach


# this is recursive approach
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def child_node(self, head, ans):
    if not head:
        return None

    temp = head

    while temp:
        ans.append(temp.val)
        if temp.child:
            child_node(temp.child, ans)
        temp = temp.next


def flatten(head):
    if not head:
        return None

    temp = head
    ans = list()
    while temp:
        ans.append(temp.val)
        if temp.child:
            child_node(temp.child, ans)
        temp = temp.next

    print(ans)
    new_ptr = new_head = Node(ans.pop(0))
    prev = None
    while len(ans):
        new_head.next = Node(ans.pop(0))
        new_head.prev = new_head
        new_head.child = None
        prev = new_head
        new_head = new_head.next

    return new_ptr

