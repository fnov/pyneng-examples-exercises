# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ivlan = input('Enter VLAN number: ')

lines = []

with open('CAM_table.txt', 'r') as file:
    for line in file:
        if line.count('.') >= 2 and line.split()[0] == ivlan:
            lines.append(line.split())


for vlan, mac, _, intf in sorted(lines, key=lambda l: int(l[0])):  # sort by int(vlan)
    print(f"{vlan:<8} {mac:19} {intf}")
