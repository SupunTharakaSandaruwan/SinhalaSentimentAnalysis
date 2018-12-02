# Read conjoined adjectives pair
# Check adjective present in seed set
# Set other adjective's polarity as different if the conjunction is "hoo"
# Set other adjective's polarity as same if the conjunction is "saha" or "haa"

import codecs


def read_file(file_name):
    file_path = "D:\\Education\\Z\\Filtered\\1CONCATENATED\\" + file_name + ".TXT"

    with codecs.open(file_path, encoding="utf-8") as fp:
        text_line = fp.readline().split('\r\n')[0]
        text_elements = str(text_line).split(" ")
        # print(text_elements)

        adjective1 = text_elements[0].split("_")[0]
        adjective2 = text_elements[2].split("_")[0]
        conjunction = text_elements[1].split("_")[0]

        match_with_seed_set(adjective1, adjective2, conjunction)

        while text_line:
            text_line = fp.readline().split('\r\n')[0]
            text_elements = str(text_line).split(" ")

            adjective1 = text_elements[0].split("_")[0]
            adjective2 = text_elements[2].split("_")[0]
            conjunction = text_elements[1].split("_")[0]

            match_with_seed_set(adjective1, adjective2, conjunction)


def match_with_seed_set(adj1, adj2, conj):
    file_path = "D:\\Education\\Z\\Results\\TEST SEED SET\\SEED_SET_TEST1.TXT"

    with codecs.open(file_path, encoding="utf-8") as fp:
        text_line = fp.readline().split('\r\n')[0]
        seed_word = str(text_line).split("\t")[0]

        if seed_word.__eq__(adj1):
            seed_polarity = str(text_line).split("\t")[1]
            predict_polaritiy(adj2, seed_polarity, conj)

        elif seed_word.__eq__(adj2):
            seed_polarity = str(text_line).split("\t")[1]
            predict_polaritiy(adj1, seed_polarity, conj)

        while text_line:
            text_line = fp.readline().split('\r\n')[0]
            seed_word = str(text_line).split("\t")[0]

            if seed_word.__eq__(adj1):
                seed_polarity = str(text_line).split("\t")[1]
                predict_polaritiy(adj2, seed_polarity, conj)

            elif seed_word.__eq__(adj2):
                seed_polarity = str(text_line).split("\t")[1]
                predict_polaritiy(adj1, seed_polarity, conj)


def predict_polaritiy(adj, seed_pol, con):
    if con.__eq__("හෝ"):
        if seed_pol.__eq__("P"):
            adj_polarity = "N"
        elif seed_pol.__eq__("N"):
            adj_polarity = "P"
    else:
        if seed_pol.__eq__("P"):
            adj_polarity = "P"
        elif seed_pol.__eq__("N"):
            adj_polarity = "N"

    print(adj + "\t" + adj_polarity)
    f = codecs.open("D:\\Education\\Z\\Filtered\\1CONCATENATED\PREDICTED_POLARITY.TXT", "a", encoding='utf-8')
    f.write(adj + "\t" + adj_polarity + "\r\n")
    f.close()


read_file("CONJOINED_ADJECTIVES__UNIQUE_SET")
