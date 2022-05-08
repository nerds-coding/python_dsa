class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_head(self, data):
        node = Node(data)

        if self.head:
            node.next = self.head

        self.head = node

    def print_all_node(self):
        while self.head:
            print(self.head.data)
            self.head = self.head.next

    def delete_node(self, data):

        temp = self.head
        prev = None

        if self.head.data == data:
            self.head = self.head.next
            return self.head

        while temp:
            if temp.data == data:
                break

            prev = temp
            temp = temp.next

        if temp.next:
            prev.next = temp.next
        else:
            prev.next = None
        return self.head

    def sort_ll(self):
        if not self.head:
            return None

        current = self.head

        while current:
            new_cur = current
            temp = current

            while temp.next:
                if new_cur.data >= temp.next.data:
                    new_cur.data, temp.next.data = temp.next.data, new_cur.data
                temp = temp.next

            current = current.next

        return self.head

    def insert_at(self, place, data):
        node = Node(data)

        if not self.head:
            return None

        temp = self.head

        while temp:
            if temp.data == place:
                break

            prev = temp
            temp = temp.next

        prev.next = node
        if temp:
            node.next = temp

        return self.head


ll = LinkedList()

ll.insert_at_head(1)
ll.insert_at_head(2)
ll.insert_at_head(6)
ll.insert_at_head(7)
ll.insert_at_head(5)
ll.insert_at_head(3)
ll.insert_at_head(4)

ll.delete_node(4)

ll.sort_ll()

ll.insert_at(7, 9)
ll.print_all_node()
