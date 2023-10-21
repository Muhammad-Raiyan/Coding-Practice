
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self) -> None:
        cur = self.top
        while cur:
            print(cur.value)
            cur = cur.next

my_stack = Stack(4)        

my_stack.print_stack()



