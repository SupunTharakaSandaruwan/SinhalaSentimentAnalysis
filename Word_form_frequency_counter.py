# 31-10-2018 | THILINA_CHATHURANGA @ Campus

import codecs
import re
import os
from collections import Counter
from collections import OrderedDict
from operator import itemgetter


def count_adjectives():

    with codecs.open("D:\\Education\\Z\\Filtered\\1CONCATENATED\\ADJECTIVES_SET.TXT", "r+", encoding='utf-8') as f:
        adj_count = Counter(f.read().split("\r\n"))

    f.close()

    sorted_adj_count = OrderedDict(sorted(adj_count.items(), key=itemgetter(1), reverse= True))
    print(sorted_adj_count)

    f = codecs.open("D:\\Education\\Z\\Filtered\\1CONCATENATED\\ADJECTIVES__UNIQUE_SET.TXT", "a", encoding='utf-8')

    for k, v in sorted_adj_count.items():
            # print(k, v)
            # f.write(str(k) + "\t" + str(v) + '\r\n')
            f.write(str(k) + '\r\n')

    f.close()


# directory_path = "D:\\Education\\Z\\Filtered-Adjectives"
# for filename in os.listdir(directory_path):
#     file_name_str = filename.title().upper().split('.')
#     count_adjectives(file_name_str[0])
#     # filename += 1
#     # print(file_name_str[0])

count_adjectives()
