# !/usr/bin/python3

for i in range(122, 96, -2):
    '''
    if 1 % 10 == 0:
        letter = chr(i)
    else:
        letter = chr(i - 32)
    '''
    print(f"{chr(i)}", end="")
    i = (i - 1) - 32
    print(f"{chr(i)}", end="")
