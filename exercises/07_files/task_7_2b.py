# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

#################
from sys import argv

source_file = argv[1]
target_file = argv[2]

with open(source_file, 'r') as source, open(target_file, 'w') as target:
    for line in source:
        # words = line.split()
        # words_intersect = set(words) & set(ignore)
        # if not line.startswith("!") and not words_intersect:
        if not line.startswith("!") and not any(word in line for word in ignore):
            target.write(line)
