
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: Node | None = None
        self.prev: Node | None = None

class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
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

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return
        to_pop = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            to_pop.prev = None
        self.length -= 1
        return to_pop
    
    def pop_first(self):
        to_pop = self.head

        if to_pop is None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            to_pop.next = None
        self.length -= 1
        return to_pop
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            return cur
        else:
            cur = self.tail
            for _ in range(self.length-index-1):
                cur = cur.prev
            return cur

    def set_value(self, index, value):
        target = self.get(index)
        if target:
            target.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.length += 1
            return True 
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        target = self.get(index)
        if target:
            prev  = target.prev
            prev.next = new_node
            new_node.next = target
            new_node.prev = prev
            target.prev = new_node
            self.length += 1
            return True
        return False
    
    def remove(self, index):
        target = self.get(index)
        if target:
            if index == 0:
                return self.pop_first()
            elif index == self.length - 1:
                return self.pop()
            else:
                prev = target.prev
                after = target.next
                target.prev = None
                target.next = None
                prev.next = after
                after.prev = prev
                return target
        return None
        
test = 0
my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.print_list()

print("Calling Pop")
print(my_dll.pop().value)
print("List after pop")
my_dll.print_list()

my_dll.prepend(2)
my_dll.prepend(3)
my_dll.prepend(4)
my_dll.prepend(5)
print("List after prepend")
my_dll.print_list()

my_dll.pop_first()
print("List after pop first")
my_dll.print_list()
print("Node at index 2")
print(my_dll.get(2).value)
my_dll.set_value(2, -2)
print("Setting new value at 2")
my_dll.print_list()
my_dll.insert(1, 6)
print("Inserting at 1 value 6")
my_dll.print_list()
print("Remove index 1")
my_dll.remove(0)
my_dll.print_list()