# 05-10-2018 | THILINA_CHATHURANGA @ HOSTEL

import codecs

no_evaluators = 3


def write_file(paragraph):
    # Regular File Path > D:\\Education\\Z\\Encoded-Corpus\\V1\\
    f = codecs.open("D:\\Education\\Z\\Results\\FINAL_POLARITIES_DETAILED.TXT", "a", encoding='utf-8')
    f.write(paragraph + "\r\n")
    f.close()
    # print("Encoded " + file_name)


def check_agreement(line):
    split_str = line.split('\t')

    # print(split_str)

    positive_count = 0
    negative_count = 0
    neutral_count = 0
    both_count = 0

    i = 0
    for i in range(no_evaluators):
        if split_str[i + 2].__eq__('P'):
            positive_count += 1
        elif split_str[i + 2].__eq__('N'):
            negative_count += 1
        elif split_str[i + 2].__eq__('B'):
            both_count += 1
        elif split_str[i + 2].__eq__('-'):
            neutral_count += 1
        else:
            print("Invalid Value")

    positive_count /= no_evaluators
    negative_count /= no_evaluators
    both_count /= no_evaluators
    neutral_count /= no_evaluators

    count_list = [positive_count, negative_count, both_count, neutral_count]
    # print(count_list)

    agreement = max(count_list)

    if agreement == positive_count:
        word_polarity = 'P'
    elif agreement == negative_count:
        word_polarity = 'N'
    elif agreement == both_count:
        word_polarity = 'B'
    elif agreement == neutral_count:
        word_polarity = '-'
    else:
        print("Invalid Value")

    detail = split_str[0] + "\t" + str(agreement) + "\t" + word_polarity
    print(detail)
    write_file(detail)


def read_file(file_name):
    file_path = "D:\\Education\\Z\\Results\\" + file_name + ".TXT"

    with codecs.open(file_path, encoding="utf-8") as fp:
        text_line = fp.readline().split('\r\n')[0]
        check_agreement(text_line)

        while text_line:
            text_line = fp.readline().split('\r\n')[0]
            check_agreement(text_line)


read_file("ADJECTIVE_EVALUATIONS")
