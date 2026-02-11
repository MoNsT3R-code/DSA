class SinglyLinkedList:

    def __init__  (self, data = None):

        self.data = data
        self.next = None

class singly_linked_list:
    
    def __init__(self):

        self.head = None

    def insert_at_the_beginning(self, data):
        
        newnod = SinglyLinkedList(data)
        newnod.next = self.head
        self.head = newnod

    def insert_at_end(self, data):

        if not self.head:
            self.head = SinglyLinkedList(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = SinglyLinkedList(data)

    def delete_from_beginning(self):

        if self.head:
            self.head = self.head.next

    def delete_from_end(self, ): 

        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None


    def insert_after(self, target, new_data):

        curr = self.head
        last_occ = None

        while curr:
            if curr.data == target:
                last_occ = None
            curr = curr.next
            if last_occ:
                newnod = SinglyLinkedList(new_data)
                newnod.next = last_occ.next
                last_occ.next = newnod
        

    def insert_before(self, next_data, new_data):

        if not self.head:
            return
        if self.head.data == next_data:
            self.insert_at_the_beginning(new_data)

        curr = self.head
        while curr.next:
            if curr.next.data == next_data:
                newnod = SinglyLinkedList(new_data)
                newnod.next = curr.next
                curr.next = newnod
                return
            curr = curr.next

    def display(self):
        no = []
        curr_nod = self.head
        while curr_nod:
            no.append(curr_nod.data)
            curr_nod = curr_nod.next
        print(no)

    
sll = singly_linked_list()
sll.insert_at_the_beginning(2)
sll.insert_at_end(3)
sll.insert_at_the_beginning(1)
sll.display()

sll.delete_from_beginning()
sll.display()
sll.delete_from_end()
sll.display()

sll.insert_at_end(3)
sll.insert_at_end(2)
sll.insert_after(2, 4)
sll.display()

sll.insert_before(2, 0)
sll.display()

def find_middle_node(self, sll):

        slow = sll.head
        fast = sll.head

        if sll.head is None:
            return None

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

        return slow.data 


sll = singly_linked_list()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)

print(find_middle_node(sll))

sll2 = singly_linked_list()
sll2.insert_at_end(1)
sll2.insert_at_end(2)
sll2.insert_at_end(3)
sll2.insert_at_end(4)

print(find_middle_node(sll2))

sll3 = singly_linked_list()
print(find_middle_node(sll3))

sll4 = singly_linked_list()
sll4.insert_at_end(10)
print(find_middle_node(sll4))
