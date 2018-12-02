# 23-07-2018 | THILINA_CHATHURANGA @ HOSTEL
# 21-10-2018 | MODIFIED

from bs4 import BeautifulSoup
import codecs
import os


def write_encoded_file(file_name, paragraph):

    # Regular File Path > D:\\Education\\Z\\Encoded-Corpus\\V1\\
    f = codecs.open("D:\\Education\\Z\\Encoded-Corpus\\V2\\" + file_name + "_EN.TXT", "a", encoding='utf-8')
    f.write(paragraph)
    f.close()
    # print("Encoded " + file_name)


# Files with text body included inside ART tag
def get_text_file_type1(file_name):
    # Tagged Corpus File Path > D:\\Education\\Z\\UCSC-Sinhala-Tagged-Corpus-V1\\UCSC Sinhala Tagged Corpus V1\\
    # News Corpus File Path > D:\\Education\\Z\\UCSC-Sinhala-News-Corpus-V1\\News Corpus_V1\\
    corpus_file_path = "D:\\Education\\Z\\UCSC-Sinhala-News-Corpus-V1\\News Corpus_V1\\" + file_name + ".TXT"

    with open(corpus_file_path, 'rb') as f:
        contents = f.read()

        soup = BeautifulSoup(contents, 'html.parser')
        # print(soup.prettify())

        if soup.find('art'):
            art_text = soup.find('art').get_text()
            # print(art_text)

        else:
            print("Skipped " + file_name)
            art_text = ""

        return art_text


# Files with text body included without tags
def get_text_file_type2(file_name):
    corpus_file_path = "D:\\Education\\Z\\UCSC-Sinhala-News-Corpus-V2\\News Corpus_V2\\" + file_name + ".TXT"

    with open(corpus_file_path, 'rb') as f:
        contents = f.read()

        soup = BeautifulSoup(contents, 'html.parser')
        # print(soup.prettify())

        if soup.get_text():
            art_text = soup.get_text()
            # print(art_text)

        else:
            print("Skipped " + file_name)
            art_text = ""

        return art_text


# directory_path = "D:\\Education\\Z\\UCSC-Sinhala-News-Corpus-V1\\News Corpus_V1"
directory_path = "D:\\Education\\Z\\UCSC-Sinhala-News-Corpus-V2\\News Corpus_V2"
for filename in os.listdir(directory_path):
    file_name_str = str(filename.title().upper().split('.')[0])
    encoded_text = get_text_file_type2(file_name_str)
    if encoded_text.__ne__(""):
        write_encoded_file(file_name_str, encoded_text)
    # filename += 1
    # print(file_name_str[0])