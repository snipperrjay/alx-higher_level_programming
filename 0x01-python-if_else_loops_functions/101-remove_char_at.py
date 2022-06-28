#!/usr/bin/python3
def remove_char_at(str, n):
    x = ""
    for k in range(len(str)):
        if k != n:
            x = x + str[k]
    return x
