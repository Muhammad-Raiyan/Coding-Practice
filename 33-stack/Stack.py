
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: Node | None = None


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

    def push(self, value):
        new_node = Node(value)
        if self.height != 0:
            new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next # type: ignore
        temp.next = None
        self.height -= 1
        return temp

my_stack = Stack(4)
my_stack.push(3)
my_stack.print_stack()
print("Popping")
my_stack.pop()
my_stack.print_stack()

