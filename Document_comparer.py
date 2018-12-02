# 20-11-2018 | THILINA_CHATHURANGA @ Hostel

# Read first file, line at a time.
# Read second file and search for above string inside it.
# If found ignore, else write them to aseperate file.


# 24-10-2018 | THILINA_CHATHURANGA @ Campus

import codecs
import re
import os

file1 = "D:\\Education\\Z\\Filtered\\1CONCATENATED\\CONJOINED_ADJECTIVES__UNIQUE_SET.TXT"
file2 = "D:\\Education\\Z\Filtered\\1CONCATENATED\\old\\old conj adj\\CONJOINED_ADJECTIVES__UNIQUE_SET_mannually_sorted.TXT"


def compare_line(file1_line):
    with codecs.open(file2, encoding="utf-8") as fp2:

        flag = 0

        file2_line = fp2.readline()
        if file2_line.__eq__(file1_line):
            # print(file1_line + " " + file2_line)
            flag = 1

        while file2_line:
            file2_line = fp2.readline()
            if file2_line.__eq__(file1_line):
                flag = 1
                break

        if flag == 0:
            print(file1_line.split('\r\n')[0])


def read_file():
    with codecs.open(file1, encoding="utf-8") as fp:
        line = fp.readline()
        compare_line(line)

        while line:
            line = fp.readline()
            compare_line(line)


read_file()

