
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
        last_node = self.tail
    
        last_node.next = new_node
        new_node.prev = last_node
        self.length += 1

    def preprend(self, value):
        pass

test = 0
my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.print_list()
