import codecs


def write_multiple_sentences_to_file(file_name, split_line):
    f = codecs.open("D:\\Education\\Z\\Split-Corpus\\" + file_name + "_SPLIT.TXT", "a", encoding='utf-8')
    array_len = len(split_line)
    print(split_line)
    for j in range(array_len):
        # print(split_line[j])
        f.write(str(split_line[j]+"\r\n"))
        print('print sentence...\n\n')


def split_into_sentences(file_name):
    corpus_file_path = "D:\\Education\\Z\\Temp_Copy\\" + file_name + "_ENCODED.TXT"

    with codecs.open(corpus_file_path, encoding="utf-8") as fp:
        line = fp.readline()
        split_str = line.split('. ')

        write_multiple_sentences_to_file(file_name, split_str);

        count = 1

        while line:
            line = fp.readline()
            split_str = line.split('. ')

            write_multiple_sentences_to_file(file_name, split_str);

            count += 1


for i in range(1):
    file_name_str = "NPED000"+str(i+1)
    split_into_sentences(file_name_str)
    i += 1
