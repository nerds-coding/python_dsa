# removing duplicat from Sorted linked list
def removeDuplicates(head):

    if not head:
        return head

    prev = head
    temp = head

    while temp.next:

        if temp.data == temp.next.data:
            # here we are note initalizing the temp
            # instead we are replacing next with next's nxt
            # then again we are checking no duplicate
            # values in straight row
            temp.next = temp.next.next
        else:
            temp = temp.next

    return head


# REMOVE DUPLICATE FROM UN-SORTED LINKED LIST


def removeDuplicates(self, head):

    if not head:
        return head

    temp = head
    count = dict()

    while temp:

        count[temp.data] = 1 + count.get(temp.data, 0)
        temp = temp.next

    temp = head

    cur = prev = Node(0)

    # Traversaing the ll and removing the value from the linked which
    # we have traversed and
    # and making new node from it

    # if the value is not presend in dict() it means we have already made the
    # node from it

    while temp:

        if count.get(temp.data):
            prev.next = Node(temp.data)
            prev = prev.next
            count.pop(temp.data)
        temp = temp.next

    return cur.next
