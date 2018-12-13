# 24-10-2018 | THILINA_CHATHURANGA @ Campus

import codecs
import re
import os

part_no = 26


def get_adjectives(response_text):
    words = re.split(' ', response_text, re.UNICODE)

    # Noise Removed | NR
    f = codecs.open("D:\\Education\\Z\\Filtered\\ADJECTIVES_NR" + str(part_no) + ".TXT", "a", encoding='utf-8')

    for word in words:
        # With findall() sometimes retrieve sentences appending the _JJ.
        # To remove that noise, if word count is not 1, take only the last word.
        if re.findall('.{1,}_JJ', word):
            if len(re.split(' ', word)) != 1:
                adj_with_noise = re.split('_JJ', word)[0]
                adj = re.split(' ', adj_with_noise)[-1]
                # adj = re.split('_JJ', last_word)[0]
            else:
                adj = re.split('_JJ', word)[0]

            f.write(str(adj) + '\r\n')

    f.close()


def scrap_adjectives(file_name):

    corpus_file_path = "D:\\Education\\Z\\Tagged-Corpus\\V2\\PART" + str(part_no) + "\\" + file_name + ".TXT"
    print('[Filtering ' + file_name + ']')

    with codecs.open(corpus_file_path, encoding="utf-8") as fp:
        line = fp.readline()
        count = 10
        while line:
            line = fp.readline()
            # print('Line' + str(count) + ' > ', line)
            get_adjectives(line)
            count += 1


directory_path = "D:\\Education\\Z\\Tagged-Corpus\\V2\\PART" + str(part_no)
for filename in os.listdir(directory_path):
    file_name_str = filename.title().upper().split('.')
    scrap_adjectives(file_name_str[0])
#edited dsfd
