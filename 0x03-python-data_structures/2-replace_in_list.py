#!/usr/bin/python3
# 2-replace_in_list.py


def replace_in_list(my_list, idx, element):
    if idx > (len(my_list) - 1) or idx < 0:
        return my_list
    else:
        my_list[idx] = element
         return my_list
