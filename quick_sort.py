# def quick_sort(my_list):
#     _quick_sort(my_list, 0, len(my_list) - 1)

# def _quick_sort(my_list, left, right):


def quick_sort_no_help(my_list):
    if len(my_list) <= 1:
        return my_list
    pivot = _pivot_picker(my_list)


def _pivot_picker(my_list):
    left = my_list[0]
    mid = my_list[len(my_list) // 2]
    right = my_list[-1]

    if left <= mid <= right or left >= mid >= right:
        return mid
    elif mid <= left <= right or mid >= left >= right:
        return left
    else:
        return right

if __name__ == '__main__':
    ml = [10, 2, 1, 4]
    ml2 = [2, 1, 3]
    ml3 = [3, 1, 2]
    ml4 = [3, 2, 1]
    ml5 = [1, 3, 2]
    ml6 = [2, 3, 1]

    print _pivot_picker(ml)
    print _pivot_picker(ml2)
    print _pivot_picker(ml3)
    print _pivot_picker(ml4)
    print _pivot_picker(ml5)
    print _pivot_picker(ml6)





