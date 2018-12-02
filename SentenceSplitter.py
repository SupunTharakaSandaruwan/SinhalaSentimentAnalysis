import codecs
import os


def write_multiple_sentences_to_file(file_name, split_line):
    f = codecs.open("D:\\Education\\Z\\Split-Corpus\\V2\\" + file_name + "_SP.TXT", "a", encoding='utf-8')
    array_len = len(split_line)
    for j in range(array_len):
        f.write(str(split_line[j]+"\r\n"))


def split_into_sentences(file_name):
    corpus_file_path = "D:\\Education\\Z\\Encoded-Corpus\\V2\\" + file_name + ".TXT"

    with codecs.open(corpus_file_path, encoding="utf-8") as fp:
        line = fp.read()
        split_str = line.split('. ')
        write_multiple_sentences_to_file(file_name, split_str);

    print("Split sentences in file " + filename)


directory_path = "D:\\Education\\Z\\Encoded-Corpus\\V2"
for filename in os.listdir(directory_path):
    file_name_str = filename.title().upper().split('.')
    split_into_sentences(file_name_str[0])
    # filename += 1
    # print(file_name_str[0])
