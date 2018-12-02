# 31-10-2018 | THILINA_CHATHURANGA @ Campus

import codecs
from collections import Counter
from collections import OrderedDict
from operator import itemgetter


def count_words():

    with codecs.open("D:\\Education\\Z\\Filtered\\1CONCATENATED\\TAGGED_CORPUS_SET.TXT", "r+", encoding='utf-8') as f:
        words = [word for line in f for word in line.split()]
        print("Total Word Count : " + str(len(words)))

    f.close()


count_words()
