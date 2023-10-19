class Node:
    def __init__(self, value) :
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    # create a new Node
    # add Node to end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    # Create new Node
    # Add Node to beginning
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
        return True

    # Removes the last node
    # Returns the node
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        
        pre = self.head
        temp = self.head
        while temp.next:
           pre = temp
           temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp

    # Removes the first Node
    # Returns the node 
    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        
        pre = self.head
        self.head = self.head.next
        pre.next = None
        self.length -= 1
        return pre

    # Create new Node
    # Insert node at index
    def insert(self, index, value):
        if self.length == 1 or index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        pre = self.get(index-1)
        cur = pre.next if pre else None

        if cur is None:
            return False
        
        new_node = Node(value)
        new_node.next = cur
        pre.next = new_node
        self.length += 1
        return True

    # Removes the Node at Index
    # Returns the Node
    def remove(self, index):
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        if index <= 0 or index >= self.length:
            return None
        pre = self.get(index-1)
        cur = pre.next
        temp = cur.next

        pre.next = temp
        cur.next = None
        self.length -= 1
        return cur
    
    # Returns the Node at Index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        target = self.head
        for _ in range(index):
            target = target.next

        return target

    # Set the Value at Index
    # Return True if successful
    # False if not successful 
    def set_value(self, index, value):
        target = self.get(index)
        if target:
            target.value = value
            return True
        return False

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        pre = None
        cur = temp
        #after = cur.next
        while cur is not None:
            after = cur.next
            cur.next = pre
            pre = cur
            cur = after

    def print_list(self):
        temp = self.head;
        print("Head:", self.head.value, "Tail:", self.tail.value, "Length:", self.length)
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")
        
    def find_middle_node(self):
        
        cur = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            cur = cur.next
            fast = fast.next.next
            
        return cur
        
    def has_loop(self):
        slow = self.head
        fast = self.head
        if slow is None:
            return False
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        return False

def find_kth_from_end(linkedlist: LinkedList, k):
    slow = linkedlist.head
    fast = linkedlist.head
    
    for i in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow

my_LL = LinkedList(4)

my_LL.print_list()

my_LL.append(5)
my_LL.print_list()

print("Popping from List")
print(my_LL.pop().value)
my_LL.print_list()

print("testing prepend")
my_LL.prepend(3)
my_LL.print_list()
my_LL.prepend(5)
my_LL.print_list()

print("pop first: ", my_LL.pop_first().value)
my_LL.print_list()

print(my_LL.get(0).value)
print(my_LL.get(1).value)
print(my_LL.get(2))
my_LL.set_value(1, 6)
my_LL.print_list()
my_LL.insert(0, 9)
my_LL.print_list()
print(my_LL.remove(0).value)
my_LL.print_list()
my_LL.append(1)
my_LL.append(4)
my_LL.print_list()
my_LL.reverse()
my_LL.print_list()
print("Middle", my_LL.find_middle_node().value)

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )