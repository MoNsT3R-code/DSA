print('Task 1')
print()

class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    
    def __init__(self):

        self.head = None

    def insert_at_beginning(self, data):

        new_node = Node(data)
        new_node.next = self.head

        if self.head:

            self.head.prev = new_node

        self.head = new_node

    def insert_at_end(self, data):

        new_node = Node(data)

        if not self.head:

            self.head = new_node
            return

        curr = self.head

        while curr.next:

            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

    def delete_from_beginning(self):

        if not self.head:

            return

        self.head = self.head.next

        if self.head:

            self.head.prev = None

    def delete_from_end(self):

        if not self.head:

            return

        if not self.head.next:

            self.head = None
            return

        curr = self.head

        while curr.next:

            curr = curr.next

        curr.prev.next = None

    def display_forward(self):

        result = []
        curr = self.head

        while curr:

            result.append(curr.data)
            curr = curr.next

        print(result)

    def display_backward(self):

        result = []
        curr = self.head

        if not curr:

            print(result)
            return

        while curr.next:

            curr = curr.next

        while curr:

            result.append(curr.data)
            curr = curr.prev

        print(result)

dll = DoublyLinkedList()

dll.insert_at_beginning(10)
dll.insert_at_end(20)
dll.insert_at_beginning(5)
dll.display_forward()

print()

dll.display_backward()
dll.delete_from_beginning()
dll.delete_from_end()

print()

dll.display_forward()

print()

print('Task 2')
print()

def reverse_list(dll):

    current = dll.head
    prev_node = None

    
    while current:

        next_node = current.next
        current.next = prev_node
        current.prev = next_node
        prev_node = current
        current = next_node
   
    dll.head = prev_node

dll = DoublyLinkedList()

dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.display_forward()

print()

reverse_list(dll)
dll.display_forward()

print()

dll.display_backward()    
