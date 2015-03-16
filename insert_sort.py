def insert_sort(my_list):
    for i in range(1, len(my_list)):
        j = i - 1
        key = my_list[i]
        while (j >= 0) and (my_list[j] > key):
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key

if __name__ == '__main__':
