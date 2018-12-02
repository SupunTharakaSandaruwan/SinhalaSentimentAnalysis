# 24-10-2018 | THILINA_CHATHURANGA @ UOR

import codecs
import re
import os

part_no = 4


def get_adjectives(response_text):
    words = re.split(' ', response_text, re.UNICODE)
    print('Split > ', str(words))

    f1 = codecs.open("D:\\Education\\Z\\Filtered\\SENTENCES_WITH_CON_ADJ_" + str(part_no) + ".TXT", "a", encoding='utf-8')
    # f2 = codecs.open("D:\\Education\\Z\\Filtered\\CONJOINED_ADJECTIVES_" + str(part_no) + ".TXT", "a", encoding='utf-8')

    for word in words:
        if re.findall('.{1,}_JJ', word):
            pre_word = words[words.index(word)-1]
            if re.findall('.{1,}_CC', pre_word):
                pre_pre_word = words[words.index(word) - 2]
                if re.findall('.{1,}_JJ', pre_pre_word):
                    pattern = pre_pre_word + " " + pre_word + " " + word
                    print(response_text)
                    f1.write(str(response_text) + '\r\n')
                    # f2.write(str(pattern) + '\r\n')

    f1.close()
    # f2.close()


def scrap_adjectives(file_name):

    corpus_file_path = "D:\\Education\\Z\\Tagged-Corpus\\V1\\PART" + str(part_no) + "\\" + file_name + ".TXT"
    print('[File Name :' + file_name)

    with codecs.open(corpus_file_path, encoding="utf-8") as fp:
        line = fp.readline()
        print('Line1 > ', line)
        get_adjectives(line)
        count = 1
        while line:
            line = fp.readline()
            print('Line' + str(count) + ' > ', line)
            get_adjectives(line)
            count += 1
            #break


# for i in range(10):
#     file_str = "politics_"+str(i+1)
#     scrap_adjectives(str(i+1), file_str)
#     i += 1
#     break

directory_path = "D:\\Education\\Z\\Tagged-Corpus\\V1\\PART" + str(part_no)
for filename in os.listdir(directory_path):
    file_name_str = filename.title().upper().split('.')
    scrap_adjectives(file_name_str[0])
    # filename += 1
    # print(file_name_str[0])
