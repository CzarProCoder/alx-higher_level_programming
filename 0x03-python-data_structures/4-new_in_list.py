#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_list1 = my_list[:]
    no_elem = len(my_list1)
    if (idx < 0):
        return my_list1
    if (idx >= no_elem):
        return my_list1
    my_list1[idx] = element
    return my_list1
