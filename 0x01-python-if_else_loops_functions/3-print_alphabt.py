#!/usr/bin/python3
for x in range(97, 123):
    if x == 113:
        continue
    if x == 101:
        continue
    print("{:c}".format(x), end='')
