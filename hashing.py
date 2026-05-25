class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = []

        for i in range(size):
            self.table.append([])

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        for x in range(self.size):
            print(self.table[x])


if __name__ == "__main__":
    h = Hashtable(10)

    h.insert(15)
    h.insert(25)
    h.insert(35)
    h.display()