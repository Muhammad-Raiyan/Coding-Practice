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
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def partition_list(self, x):
        if self.head is None:
            return 
        lessThanTargetList = None
        greaterThanTargetList = None
        itr = self.head
        while itr:
            if itr.value < x:
                if lessThanTargetList is None:
                    lessThanTargetList = LinkedList(itr.value)
                else:
                    lessThanTargetList.append(itr.value)
            else:
                if greaterThanTargetList is None:
                    greaterThanTargetList = LinkedList(itr.value)
                else:
                    greaterThanTargetList.append(itr.value)
            itr = itr.next
        temp = lessThanTargetList.head
        while temp.next is not None:
            temp = temp.next
        if greaterThanTargetList is not None:
            temp.next = greaterThanTargetList.head
        self.head = lessThanTargetList.head
    

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(11)

print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10


"""
    EXPECTED OUTPUT:
    ----------------
    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10
    
"""
