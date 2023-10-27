class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        min_index = index
        while min_index < len(self.heap):
            left = self._left_child(min_index)
            right = self._right_child(min_index)
            if left < len(self.heap) and self.heap[min_index] > self.heap[left]:
                min_index = left
            if right < len(self.heap) and self.heap[min_index] > self.heap[right]:
                min_index = right

            if min_index != index:
                self._swap(min_index, index)
                index = min_index
            else:
                return

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        parent = self._parent(current)
        while current > 0 and self.heap[current] < self.heap[parent]:
            self._swap(parent, current)
            current = parent
            parent = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        to_pop = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return to_pop


my_heap = MinHeap()

my_heap.insert(10)
print(my_heap.heap)

my_heap.insert(15)
my_heap.insert(12)
print(my_heap.heap)

my_heap.insert(5)
print(my_heap.heap)
