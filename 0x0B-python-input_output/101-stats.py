#!/usr/bin/python3

"""
Script to read stdin line by line and computes metrics

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
total file size and
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500

format: File size: <total size>
format: <status code (in ascending order)>: <number>
status codes should be printed in ascending order
"""


import sys


class Magic:
    """
    Class to generates instances with dict and size
    """
    def __init__(self):
        """
        Init method
        """
        self.dic = {}
        self.size = 0

    def init_dic(self):
        """
        Initialize dict
        """
        self.dic['200'] = 0
        self.dic['301'] = 0
        self.dic['400'] = 0
        self.dic['401'] = 0
        self.dic['403'] = 0
        self.dic['404'] = 0
        self.dic['405'] = 0
        self.dic['500'] = 0

    def add_status_code(self, status):
        """
        Method to add repeated number to the status code
        """
        if status in self.dic:
            self.dic[status] += 1

    def print_info(self, sig=0, frame=0):
        """
        print status code
        """
        print("File size: {:d}".format(self.size))
        for key in sorted(self.dic.keys()):
            if self.dic[key] is not 0:
                print("{}: {:d}".format(key, self.dic[key]))


if __name__ == "__main__":
    magic = Magic()
    magic.init_dic()
    nlines = 0

    try:
        for line in sys.stdin:
            if nlines % 10 == 0 and nlines is not 0:
                magic.print_info()

            try:
                list_line = [x for x in line.split(" ") if x.strip()]
                magic.add_status_code(list_line[-2])
                magic.size += int(list_line[-1].strip("\n"))
            except:
                pass
            nlines += 1
    except KeyboardInterrupt:
        magic.print_info()
        raise
    magic.print_info()


"""
import sys


def print_size_and_codes(size, stat_codes):
    print("File size: {:d}".format(size))
    for key, value in sorted(stat_codes.items()):
        if value:
            print("{:s}: {:d}".format(key, value))


def parse_stdin_and_compute():
    size = 0
    lines = 0
    stat_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                  "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            fields = list(map(str, line.strip().split(" ")))
            size += int(fields[-1])
            if fields[-2] in stat_codes:
                stat_codes[fields[-2]] += 1
            lines += 1
            if lines % 10 == 0:
                print_size_and_codes(size, stat_codes)
    except KeyboardInterrupt:
        print_size_and_codes(size, stat_codes)
        raise

    print_size_and_codes(size, stat_codes)


parse_stdin_and_compute()
    """
