
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def swap_first_last_pointers(self):
        temp_head = self.head.next
        temp_tail = self.tail.prev
        if self.length <= 1:
            return True
        self.head.next = None
        self.head.prev = temp_tail

        temp_tail.next = self.head
        self.tail.prev = None
        
        self.tail.next = temp_head
        temp_head.prev = self.tail
        
        self.head = temp_head.prev
        self.tail = temp_tail.next

    def swap_first_last(self):    
        if self.head is None:
            return True
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp
    

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)


print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.swap_first_last()


print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before swap_first_last():
    1
    2
    3
    4

    DLL after swap_first_last():
    4
    2
    3
    1

"""

