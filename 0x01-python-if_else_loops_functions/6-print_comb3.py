#!/usr/bin/python3
i = 0
while i < 10:
    j = i + 1
    while j < 10 and j != i:
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}, ".format(i, j), end="")
        j += 1
    i += 1
