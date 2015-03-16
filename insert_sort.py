def insert_sort(my_list):
    for i in range(1, len(my_list)):
        j = i - 1
        key = my_list[i]
        while (j >= 0) and (my_list[j] > key):
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key

if __name__ == '__main__':
    import timeit

    best_list = [i for i in range(5000)]
    worst_list = [i for i in range(5000)][::-1]

    def best_case():
        return insert_sort(best_list)

    def worst_case():
        return insert_sort(worst_list)

    print "Best case 5000 in order: {}".format(
        timeit.timeit('best_case()', setup='from __main__ import best_case',
                      number=100)
    )
    print "Best case 5000 reverse order: {}".format(
        timeit.timeit('worst_case()', setup='from __main__ import worst_case',
                      number=100)
    )
