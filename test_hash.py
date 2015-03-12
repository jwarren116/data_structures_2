from hash import HashTable
import io


words = []

with io.open('/usr/share/dict/words', 'r') as word_file:
    words = word_file.readlines()


def test_hash():
    t = HashTable()
    t.set('coffee', 'coffee')
    assert t.get('coffee') == 'coffee'


def test_duplicate_hash_val():
    t = HashTable()
    t.set('bob', 'bob')
    t.set('obb', 'obb')
    assert t.get('bob') == 'bob'
    assert t.get('obb') == 'obb'


def test_word_file():
    t = HashTable()
    for word in words:
        t.set(word, word)
    assert t.get(words[654]) == words[654]
    assert t.get(words[3541]) == words[3541]
    assert t.get(words[6541]) == words[6541]
