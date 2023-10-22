
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1


    def print_quqeue(self) -> None:
        cur = self.first
        while cur:
            print(cur.value)
            cur = cur.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
        else:
            self.last.next = new_node

        self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.first is None:
            return None
        
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1

        return temp

my_q = Queue(4)
my_q.print_quqeue()

print("Enqueue")
my_q.enqueue(5)
my_q.enqueue(6)
my_q.print_quqeue()

print("Dequeue: ", my_q.dequeue().value)
my_q.print_quqeue()

