#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    values = list(a_dictionary.values())
    keys = list(a_dictionary.keys())
    new_values = list(map(lambda x: x * 2, values))
    new_dictionary = {}
    index = 0
    for key in keys:
        new_dictionary[key] = new_values[index]
        index += 1
    return new_dictionary
