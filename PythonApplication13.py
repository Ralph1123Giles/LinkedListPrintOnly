class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def append_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None:
                raise IndexError("Position out of bounds")
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node 

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        if not self.head:
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == key:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

ll = LinkedList()
for i in range(5):
    ll.append(i)
ll.prepend(-1)
ll.delete_node(5)
print(list(ll))