#!/usr/bin/python3
def safe_print_list_integers(my_list=None, x=0):
    if my_list is None:
        my_list = []

    count = 0

    for i in range(0, x):
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1

        except (IndexError, ValueError, TypeError):
            pass
    print()
    return count
