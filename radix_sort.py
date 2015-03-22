def int_radix(mylist):
    '''
    Sorts a list of ints by looking at the 1's place,
    the 10's, 100's, etc.
    '''
    for i in mylist:
        if (type(i) != int) or (i < 0):
            return 'Please input a valid list'
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
