
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        sb = ""
        if self.prev:
            sb += (str(self.prev.value) + " <- ")
        sb += (str(self.value) + " -> ")
        if self.next:
            sb += (str(self.next.value))
        return sb
        

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
        

    def reverse(self):
        if self.length <= 1:
            return True

        new_head = self.head
        cur = self.head.next
        after = cur
        new_tail = new_head

        while cur:
            after = cur.next
            new_tail = cur.prev

            cur.prev, cur.next = new_head.prev, new_head
            new_tail.next = after
            new_head.prev = cur
            if after:
                after.prev = new_tail

            new_head = cur
            cur = after

        self.head, self.tail = new_head, new_tail
        # 1 - 2 - 3 - 4
        # 2 - 1 - 3 - 4
        # 3 - 2 - 1 - 4
    
    def reverse_inline(self):
        temp = self.head
        while temp is not None:
            # swap the prev and next pointers of node points to
            print("Before Swap\nTemp: ", temp, "\nPrev: ", temp.prev, "\nNext: ", temp.next)
            temp.prev, temp.next = temp.next, temp.prev

            print("After Swap\nTemp: ", temp, "\nPrev: ", temp.prev, "\nNext: ", temp.next) 
            # move to the next node
            temp = temp.prev
            
        # swap the head and tail pointers
        self.head, self.tail = self.tail, self.head


        


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse_inline()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before reverse():
    1
    2
    3
    4
    5

    DLL after reverse():
    5
    4
    3
    2
    1

"""

    