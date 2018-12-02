# 31-10-2018 | THILINA_CHATHURANGA @ Campus

import codecs
import re
import os

# ADVERBS       >> _RB
# COM_NOUN_M    >> _NNM
# COM_NOUN_F    >> _NNF
# COM_NOUN_N    >> _NNN
# PROP_NOUN_ANI >> _NNPA
# PROP_NOUN_IN  >> _NNPI

# part_no = 1
word_form = "CONJUNCTIONS"
word_form_tag = '_CC'


def get_words(response_text):
    words = re.split(' ', response_text, re.UNICODE)

    # Noise Removed | NR
    f = codecs.open("D:\\Education\\Z\\Filtered\\" + word_form + "_NR" + str(part_no+1) + ".TXT", "a", encoding='utf-8')

    for word in words:
        # With findall() sometimes retrieve sentences appending the _JJ.
        # To remove that noise, if word count is not 1, take only the last word.
        if re.findall('.{1,}' + word_form_tag, word):
            if len(re.split(' ', word)) != 1:
                adj_with_noise = re.split(word_form_tag, word)[0]
                adj = re.split(' ', adj_with_noise)[-1]
                # adj = re.split(word_form, last_word)[0]
            else:
                adj = re.split(word_form_tag, word)[0]

            f.write(str(adj) + '\r\n')

    f.close()


def scrap_file(file_name):

    corpus_file_path = "D:\\Education\\Z\\Tagged-Corpus\\V1\\PART" + str(part_no+1) + "\\" + file_name + ".TXT"
    print('[Filtering ' + file_name + ']')

    with codecs.open(corpus_file_path, encoding="utf-8") as fp:
        line = fp.readline()
        count = 10
        while line:
            line = fp.readline()
            # print('Line' + str(count) + ' > ', line)
            get_words(line)
            count += 1


for part_no in range(5):
    directory_path = "D:\\Education\\Z\\Tagged-Corpus\\V1\\PART" + str(part_no+1)
    for filename in os.listdir(directory_path):
        file_name_str = filename.title().upper().split('.')
        scrap_file(file_name_str[0])
