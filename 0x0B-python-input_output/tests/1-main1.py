#!/usr/bin/python3

"""
Test module
"""

write_file = __import__('1-write_file').write_file


def main():
    write_file("file2", "This is just some random test file")


main()
