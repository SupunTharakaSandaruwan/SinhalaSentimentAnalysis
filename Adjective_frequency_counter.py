# 24-10-2018 | THILINA_CHATHURANGA @ Campus

import codecs
import re
import os
from collections import Counter
from collections import OrderedDict
from operator import itemgetter


# def concatenate_files():
#     with codecs.open("D:\\Education\\Z\\Filtered-Adjectives\\", "w", encoding='utf-8') as outfile:
#         for fname in filenames:
#             with codecs.open("", encoding='utf-8') as infile:


def count_adjectives():

    with codecs.open("D:\\Education\\Z\\Filtered\\1CONCATENATED\\ADJECTIVES_SET.TXT", "r+", encoding='utf-8') as f:
        adj_count = Counter(f.read().split("\r\n"))

    f.close()

    sorted_adj_count = OrderedDict(sorted(adj_count.items(), key=itemgetter(1), reverse= True))
    print(sorted_adj_count)

    f = codecs.open("D:\\Education\\Z\\Filtered\\1CONCATENATED\\ADJECTIVES_SET_COUNT.TXT", "a", encoding='utf-8')

    for k, v in sorted_adj_count.items():
            # print(k, v)
            f.write(str(k) + "\t" + str(v) + '\r\n')

    f.close()


count_adjectives()
