import codecs


def write_multiple_sentences_to_file(file_name, split_line):
    f = codecs.open("D:\\Education\\Z\\Split-Corpus\\" + file_name + "_SPLIT.TXT", "a", encoding='utf-8')
    array_len = len(split_line)
    print(split_line)
    for j in range(array_len):
        f.write(str(split_line[j]+"\r\n"))


def split_into_sentences(file_name):
    corpus_file_path = "D:\\Education\\Z\\Encoded-Corpus\\" + file_name + "_ENCODED.TXT"

    with codecs.open(corpus_file_path, encoding="utf-8") as fp:
        line = fp.read()
        split_str = line.split('. ')
        write_multiple_sentences_to_file(file_name, split_str);


for i in range(9):
    file_name_str = "NPED000"+str(i+1)
    split_into_sentences(file_name_str)
    i += 1

for j in range(i, 34):
    file_name_str = "NPED00"+str(j+1)
    split_into_sentences(file_name_str)
    j += 1

for k in range(9):
    file_name_str = "NPFEAHCI000"+str(k+1)
    split_into_sentences(file_name_str)
    k += 1

for m in range(k, 3):
    file_name_str = "NPFEAHCI00"+str(m+1)
    split_into_sentences(file_name_str)
    m += 1
