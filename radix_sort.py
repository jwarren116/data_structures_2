#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def int_radix(mylist):
    '''
    Sorts a list of ints by looking at the 1's place,
    the 10's, 100's, etc.
    '''
    for i in mylist:
        if (type(i) != int) or (i < 0):
            raise TypeError('Please input valid integers')
    if len(mylist) > 0:
        max_list = max(mylist)
        tens = 1
        num_buckets = []
        for i in range(10):
            num_buckets.append([])
        while max_list >= tens:
            for item in mylist:
                bucket = (item % (tens * 10) / tens)
                num_buckets[bucket].append(item)
            buff = []
            for bucket in num_buckets:
                while len(bucket) > 0:
                    buff.append(bucket.pop(0))
            mylist = buff
            tens *= 10
        return mylist


def str_radix(mylist):
    '''Sorts a list of strings in lexicographic order'''
    # return original list if it only contains one item
    if len(mylist) <= 1:
        return mylist
    longest = 0
    for string in mylist:
        if len(string) > longest:
            longest = len(string)
    # interim buckets for sorting
    buckets = [[] for i in range(27)]
    for place in reversed(range(0, longest)):
        for string in mylist:
            index = 0 # properly sort shorter strings into 0 index
            if place < len(string):
                # put string in bucket based on ordinal value of
                # iteration index, minus 96 (ordinal value 'a' - 1)
                index = ord(string[place]) - 96
            buckets[index].append(string)
        del mylist[:]
        for bucket in buckets:
            mylist.extend(bucket)
            del bucket[:]
    return mylist


if __name__ == '__main__':
    l = ['tooth', 'dog', 'apple', 'rad', 'A', 'the', 'a', 'z', 'Peter']
    print l
    l = str_radix(l)
    print l
    