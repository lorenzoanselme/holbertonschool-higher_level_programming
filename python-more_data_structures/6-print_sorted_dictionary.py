#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary.keys())
    for i in sorted_list:
        print("{}: {}".format(i, a_dictionary[i]))
