#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda x: replace if x == search else e, my_list))
