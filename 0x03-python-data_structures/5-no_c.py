#!/usr/bin/python3
def no_c(my_string):
    count = 0
    new_string = my_string[:]
    for index in range(len(my_string)):
        if my_string[index] == 'c' or my_string[index] == 'C':
            new_string = new_string[:index - count] + my_string[(index + 1):]
            count += 1
    return new_string
