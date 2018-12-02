import codecs
from bs4 import BeautifulSoup


def scrap_adjectives(file_no, file_name):
    corpus_file_path = "D:\\Education\\Z\\"+file_name+".txt"

    with open(corpus_file_path, 'rb') as f:
        contents = f.read()

        print('[File No:' + file_no + ']')

        soup = BeautifulSoup(contents, 'html.parser')
        #print(soup.prettify())

        text_art = soup.find('art')
        print(text_art.get_text())

    # with codecs.open(corpus_file_path, encoding="utf-8") as fp:
    #     line = fp.readline()
    #     print('Line 1 > ', line)
    #     count = 1
    #     while line:
    #         line = fp.readline()
    #         count += 1
    #         #break

for i in range(9):
    file_str = "politics_"+str(i+1)
    scrap_adjectives(str(i+1), file_str)
    i += 1
    #break



