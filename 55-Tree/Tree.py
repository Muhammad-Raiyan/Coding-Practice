class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value) -> None:
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        cur_parent = self.root
        while True:
            if new_node.value == cur_parent.value:
                return False
            if new_node.value < cur_parent.value:
                if cur_parent.left:
                    cur_parent = cur_parent.left
                else:
                    cur_parent.left = new_node
                    return True
            else:
                if cur_parent.right:
                    cur_parent = cur_parent.right
                else:
                    cur_parent.right = new_node
                    return True

    def contains(self, value):
        cur_node = self.root
        while cur_node is not None:
            if value < cur_node.value:
                cur_node = cur_node.left
            elif value > cur_node.value:
                cur_node = cur_node.right
            else:
                return True
        return False

    def BFS(self):
        res = []
        my_q = []
        my_q.append(self.root)
        while len(my_q) > 0:
            curret_node = my_q.pop(0)
            res.append(curret_node.value)
            if curret_node.left is not None:
                my_q.append(curret_node.left)
            if curret_node.right is not None:
                my_q.append(curret_node.right)
        return res

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)

        return results

    def traverse_pre_order(self, node):
        pass


my_tree = BinarySearchTree()

print(my_tree.root)

my_tree.insert(47)
my_tree.insert(21)

print("After insert: ", my_tree.root.left.value)

print(my_tree.contains(21))
print(my_tree.contains(23))

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())
print(my_tree.dfs_pre_order())
