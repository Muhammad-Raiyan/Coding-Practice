class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    

    def print_rest(self, node):
        cur = node
        while cur:
            print(cur.value, end="->")
            cur = cur.next
        print()

    def make_empty(self):
        self.head = None
        self.length = 0
    
    def reverse_between(self, start_index, end_index):
        if self.length <= 1:
            return None
        pre = None
        cur = self.head
        
        for i in range(start_index):
            pre = cur
            cur = cur.next
        
        prev_tail = pre
        new_head = cur
        
        prev = None
        start_node = cur
        after = start_node.next
        index = start_index    
        while start_node is not None and index <= end_index:
            start_node.next = prev
            prev = start_node
            start_node = after
            if after:
                after = after.next
            index += 1
        print("Index: ", index)
        if start_node:
            new_head.next = start_node 
            print("start_node", start_node.value)
        #print("prev", pre.value)
            #self.print_rest(prev)
        if prev_tail:
            prev_tail.next = prev
        else:
            self.head = prev
            
        
            

       
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

linked_list.reverse_between(1,3)

print("Reversed sublist (1, 3): ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
