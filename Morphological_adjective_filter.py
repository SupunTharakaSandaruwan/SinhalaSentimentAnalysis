# 20-11-2018 | THILINA_CHATHURANGA @ Hostel
# Read adjective list.
# Find adjectives with stems at the start of the word.
# Remove the stem and evaluate the polarity change.

import codecs

adj_file = "D:\\Education\\Z\\Filtered\\1CONCATENATED\\ADJECTIVES__UNIQUE_SET.TXT"

stem_set_1 = ['අ']  # 1 element length stems
stem_set_2 = ['අප', 'අව', 'දු', 'නි', 'නො', 'වි']  # 2 elements length stems
stem_set_3 = ['දුර්', 'නිර්']  # 3 elements length stems


def search_adjective(line_substring, line_string):
    f = codecs.open("D:\\Education\\Z\\Filtered\\1CONCATENATED\MORPHOLOGICALLY_RELATED_ADJECTIVES.TXT", "a", encoding='utf-8')

    with codecs.open(adj_file, encoding="utf-8") as fp:
        line = fp.readline()
        if line.__eq__(line_substring):
            print(line.split('\r\n')[0] + " " + line_string)
            f.write(line.split('\r\n')[0] + "\t" + line_string + "\r\n")

        while line:
            line = fp.readline()
            if line.__eq__(line_substring):
                print(line.split('\r\n')[0] + " " + line_string)
                f.write(line.split('\r\n')[0] + "\t" + line_string + "\r\n")

    f.close()


def check_line(line_string):
    # print(line_string)
    # print(line_string.split())

    if str(line_string[0:1]) in stem_set_1:
        search_adjective(str(line_string[1:]), line_string.split('\r\n')[0])

    if str(line_string[0:2]) in stem_set_2:
        search_adjective(str(line_string[2:]), line_string.split('\r\n')[0])

    if str(line_string[0:4]) in stem_set_3:
        search_adjective(str(line_string[4:]), line_string.split('\r\n')[0])


def read_file():
    with codecs.open(adj_file, encoding="utf-8") as fp:
        line = fp.readline()
        check_line(line)

        while line:
            line = fp.readline()
            check_line(line)


read_file()

