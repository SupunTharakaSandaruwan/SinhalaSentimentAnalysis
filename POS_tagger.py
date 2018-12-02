# 21-07-2018 | THILINA_CHATHURANGA @ HOSTEL

import requests
from bs4 import BeautifulSoup
import codecs
import re
import os
import pyttsx3


part_no = 16


def call_pos_tagger(line):
    pos_tagger_url = "http://173.214.171.141:8080/SNLP/snlp/SPOS/tagger"

    data = {'sentence': line}
    page = requests.post(pos_tagger_url, data)
    page_content = page.content
    response = BeautifulSoup(page_content, 'html.parser')
    response_text = response.find('response')
    print('Tagged > ', response_text.get_text())
    return response_text.get_text()


def write_tagged_file(file_name, sentence):

    f = codecs.open("D:\\Education\\Z\\Tagged-Corpus\\V2\\PART" + str(part_no) + "\\" + file_name + "_TG.TXT", "a", encoding='utf-8')
    f.write(str(sentence)+"\r\n")
    f.close()


def get_text(file_name):

    corpus_file_path = "D:\\Education\\Z\\Split-Corpus\\V2\\PART" + str(part_no) + "\\" + file_name + ".TXT"
    # print('[File No:' + file_no + ']')

    with codecs.open(corpus_file_path, encoding="utf-8") as fp:
        line = fp.readline()
        if len(line) >= 10:
            print('Line1 > ', line)
            write_tagged_file(file_name, call_pos_tagger(line))
        count = 1

        while line:
            line = fp.readline()
            if len(line) >= 10:
                print('Line' + str(count) + ' > ', line)
                write_tagged_file(file_name, call_pos_tagger(line))
            count += 1
            # break


directory_path = "D:\\Education\\Z\\Split-Corpus\\V2\\PART" + str(part_no)
for filename in os.listdir(directory_path):
    file_name_str = filename.title().upper().split('.')
    get_text(file_name_str[0])

speech_engine = pyttsx3.init()
speech_engine.say("Hey Thilyna. Part of Speech tagging Program Completed Successfully. Start next part.")
speech_engine.runAndWait()
    # filename += 1
    # print(file_name_str[0])