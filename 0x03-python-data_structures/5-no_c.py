#!/usr/bin/python3
def no_c(my_string):
    ret = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            ret += elements
    return ret
