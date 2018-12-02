import os
import codecs

directory_path = "D:\\Education\\Z\\Tagged-Corpus\\All"
# directory_path = "D:\\Education\\Z\\Filtered\\ADJECTIVES"
# directory_path = "D:\\Education\\Z\Filtered\\CONJOINED ADJECTIVES"
content = ""

for file_name in os.listdir(directory_path):
    # file_name_str = filename.title().upper().split('.')
    print(file_name)
    with codecs.open(directory_path + "\\" + file_name, "r+", encoding='utf-8') as f:
        content = content + f.read()

codecs.open("D:\\Education\\Z\\Filtered\\1CONCATENATED" + "\\TAGGED_CORPUS_SET.TXT", "a", encoding='utf-8').write(content)
