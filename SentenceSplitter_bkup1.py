import codecs


def write_multiple_sentences_to_file(file_name, split_line):
    f = codecs.open("D:\\Education\\Z\\Split-Corpus\\" + file_name + "_SPLIT.TXT", "a", encoding='utf-8')
    for j in range(len(split_line)):
        f.write(split_line[j]+'\n')


def write_file(file_name, sentence):
    f = codecs.open("D:\\Education\\Z\\Split-Corpus\\" + file_name + "_SPLIT.TXT", "a", encoding='utf-8')
    f.write(str(sentence)+'\n\n')


def split_into_sentences(file_name):
    corpus_file_path = "D:\\Education\\Z\\Temp_Copy\\" + file_name + "_ENCODED.TXT"
    # print('[File No:' + file_no + ']')

    with codecs.open(corpus_file_path, encoding="utf-8") as fp:
        line = fp.readline()
        # print('Line1 > ', line)
        split_str = line.split('. ')

        write_multiple_sentences_to_file(file_name, split_str);

        # for x in range(len(split_str)):
        #     print(split_str[x])
        #     write_file(file_name, split_str[x])

        count = 1

        while line:
            line = fp.readline()
            # print('Line' + str(count) + ' > ', line)
            split_str = line.split('. ')

            write_multiple_sentences_to_file(file_name, split_str);

            # for x in range(len(split_str)):
            #     print(split_str[x])
            #     write_file(file_name, split_str[x])

            count += 1
            #break


for i in range(1):
    file_name_str = "NPED000"+str(i+1)
    split_into_sentences(file_name_str)
    i += 1
    # break