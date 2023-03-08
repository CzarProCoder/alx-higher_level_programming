#!/usr/bin/python3

def remove_char_at(str, n):
    str_index = 0
    new_index = 0
    new_str = ""
    for i in str:
        if str_index != n:
            new_str[new_index] = i
            new_index += 1
        str_index += 1
    return new_str
