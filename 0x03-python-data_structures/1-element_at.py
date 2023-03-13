#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    no_elem = len(my_list)
    if idx >= no_elem:
        return None
    return (my_list[idx])
