#!/usr/bin/python3
""" Function that reads a text file (UTF8) and print it """


def read_file(filename=""):
    """Read text file with UTF-8"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
