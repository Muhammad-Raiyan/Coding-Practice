class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                return self.data_map[index][i][1]

    def keys(self):
        keys = []

        for item in self.data_map:
            if item:
                for key_val in item:
                    keys.append(key_val[0])

        return keys


my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)
my_hash_table.set_item("lumber", 70)

my_hash_table.print_table()


print("Bolts:", my_hash_table.get_item("bolts"))
print("Washers:", my_hash_table.get_item("washers"))
print("Lumber:", my_hash_table.get_item("lumber"))

print(my_hash_table.keys())
