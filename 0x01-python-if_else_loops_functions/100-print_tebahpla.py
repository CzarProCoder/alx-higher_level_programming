# !/usr/bin/python3

i = 122
while i > 96:
    if i % 2 != 0:
        i -= 32
    print("{}".format(chr(i)), end="")
    if i < 90:
        i += 32
    i -= 1
