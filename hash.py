class HashItem(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    def __init__(self, tablesize=1024):
        self.table = []
        for i in range(tablesize):
            self.table.append(list())

    def hash(self, key):
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val % len(self.table)

    def get(self, key):
        hashed_key = self.hash(key)
        for i in self.table[hashed_key]:
            if i[0] == key:
                return i[1]
        else:
            raise IndexError('Key not in bucket')

    def set(self, key, val):
        hashed_key = self.hash(key)
        self.table[hashed_key].append((key, val))

# if __name__ == '__main__':
#     import io
#     words = []
#     with io.open('/usr/share/dict/words', 'r') as word_file:
#         words = word_file.readlines()

#     t = HashTable()
#     # for word in words:
#     #     t.set(word, word)

#     t.set('thing', 'bob')
#     print t.get('hominy')
#     # print "bucket 600: {}".format(t.table[600])
#     # print "word 654: {}".format(words[654])
#     # print "word 65410: {}".format(words[65410])
