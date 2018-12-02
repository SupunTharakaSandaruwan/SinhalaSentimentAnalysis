# 22-10-2018 | THILINA_CHATHURANGA @ UOR

import codecs
import re
import os

part_no = 5

conjunctions = ['ද', 'හා', 'සහ', 'හෝ', 'එහෙත්', 'සමඟ', 'නමුත්', 'සමග', 'යැයි', 'හරි', 'ඒත්', 'එක්ක', 'දැයි',
                'නැත්නම්', 'ඇතත්', 'නැතහොත්', 'නැතැයි', 'නැතිනම්', 'නොහොත්', 'එහෙනම්', 'නමුදු', 'හැබැයි',
                'අතරම', 'ලදැයි', 'නැතත්', 'කැටුව', 'එක්කෝ', 'එනමුත්', 'නැතොත්']


def get_adjectives(response_text):
    words = re.split(' ', response_text, re.UNICODE)
    print('Split > ', str(words))

    f = codecs.open("D:\\Education\\Z\\Filtered\\NEW_CONJOINED_ADJECTIVES_" + str(part_no) + ".TXT", "a", encoding='utf-8')

    for word in words:
        if re.findall('.{1,}_JJ', word):
            pre_word = words[words.index(word)-1]
            if re.findall('.{1,}', pre_word):
                con = pre_word.split('_')[0]
                if con in conjunctions:
                    pre_pre_word = words[words.index(word) - 2]
                    if re.findall('.{1,}_JJ', pre_pre_word):
                        pattern = pre_pre_word + " " + pre_word + " " + word
                        print(pattern)
                        f.write(str(pattern) + '\r\n')

    f.close()


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
