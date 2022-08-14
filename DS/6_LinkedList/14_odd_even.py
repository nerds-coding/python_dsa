# https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list5035/1?page=1&difficulty[]=-2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&curated[]=7&sortBy=submissions


def divide(self, N, head):

    if not head or not head.next:
        return head

    # making 2 different ll for ODD and EVEN
    even = Node(-1)
    odd = Node(-1)

    even_ptr = even
    odd_ptr = odd

    temp = head

    while temp:

        if temp.data & 1:
            odd_ptr.next = temp
            odd = odd_ptr.next
        else:
            even_ptr.next = temp
            even_ptr = even.ptr.next
        temp = temp.next

    # if even.next is none
    # it means there is only odd values in given LL
    if even.next:
        # assigning the last even to first odd (odd.next b'coz first is -1)
        even_ptr.next = odd.next

        # odd_ptr is been moved to back
        # thus assigining the odd's last to None
        odd_ptr.next = None
        return even.next
    return odd.next
