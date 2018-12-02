# 24-10-2018 | THILINA_CHATHURANGA @ Campus

import codecs
import re
import os


part_no = 3


def get_adjectives(response_text):
    words = re.split(' ', response_text, re.UNICODE)
    # print('Split > ', str(words))

    f = codecs.open("D:\\Education\\Z\\Filtered\\ADJECTIVES_" + str(part_no) + "noisermvd.TXT", "a", encoding='utf-8')

    for word in words:
        if re.findall('.{1,}_JJ', word):
            if len(re.split(' ', word)) != 1:
                last_word = re.split(' ', word)[-1]
                adj = re.split('_JJ ', last_word)[0]
            else:
                adj = re.split('_JJ ', word)[0]
                # print(adj)

            f.write(str(adj) + '\r\n')

    f.close()


def scrap_adjectives(file_name):
    # corpus_file_path = "D:\\Education\\Z\\politics_2.txt"

    corpus_file_path = "D:\\Education\\Z\\Tagged-Corpus\\V1\\PART" + str(part_no) + "\\" + file_name + ".TXT"
    print('[Filtering ' + file_name + ']')

    with codecs.open(corpus_file_path, encoding="utf-8") as fp:
        line = fp.readline()
        count = 10
        while line:
            line = fp.readline()
            # print('Line' + str(count) + ' > ', line)
            get_adjectives(line)
            count += 1
            #break


# for i in range(9):
#     file_str = "NPED000"+str(i+1)+"_ENCODED"
#     scrap_adjectives(str(i+1), file_str)
#     i += 1
#     # break

directory_path = "D:\\Education\\Z\\Tagged-Corpus\\V1\\PART" + str(part_no)
for filename in os.listdir(directory_path):
    file_name_str = filename.title().upper().split('.')
    scrap_adjectives(file_name_str[0])
    # filename += 1
    # print(file_name_str[0])
