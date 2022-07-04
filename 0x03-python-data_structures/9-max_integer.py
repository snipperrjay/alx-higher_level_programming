#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_value = my_list[0]
        for index in range(1, len(my_list)):
            if my_list[index] > max_value:
                max_value = my_list[index]
        return max_value
