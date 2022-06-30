#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = len(sys.argv) - 1
    result = 0
    for index in range(i):
        result += int(sys.argv[index + 1])
    print(result)
