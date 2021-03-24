def reverse(list):
    for lst in list:
        lst.reverse()
    list.reverse()
    return list
reverse([[1, 2], [3, 4], [5, 6, 7]])