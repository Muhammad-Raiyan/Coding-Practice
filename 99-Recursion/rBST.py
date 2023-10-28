class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def __r_contains(self, current_node, value):
        pass

    def r_contains(self, value):
        return self.__r_contains(self.root, value)
