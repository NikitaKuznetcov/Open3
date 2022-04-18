import os
from pprint import pprint
from os import path

def create_temp(file_name):
    with open(file_name, 'rt', encoding='utf-8') as f1:
        name = f1.name
        data = f1.read()
        by_line = list(data.split('\n'))
        count = len(by_line)
        new_text = [name, count, by_line]

    return new_text

a = create_temp('1.txt')
b = create_temp('2.txt')
c = create_temp('3.txt')



def create_list(temp):
    from operator import itemgetter
    new_list = sorted((temp), key=itemgetter(1))
    return new_list

libr_ = create_list([a, b, c])


def create_new_file(bibl):
    with open('myfile.txt', 'w', encoding='utf-8') as f4:
        for files in bibl:
            n = files
            f4.write(n[0] + '\n')
            f4.write(str(n[1]) + '\n')
            for every_string in n[2]:
                f4.write(every_string + '\n')
    return
create_new_file(libr_)