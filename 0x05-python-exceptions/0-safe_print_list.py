#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    index = 0

    while index < x:
        try:
            print(f"{my_list[index]}", end="")
        except Exception:
            break
        else:
            index += 1
    print()
    return (index)
