class HashItem(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    def __init__(self, tablesize=1024):
        self.table = []
        for i in range(tablesize):
            self.table.append(tuple())

t = HashTable(100)
t.table[5] = ('hash', 'hash')
print t.table
