# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

###################
is_valid = False
while not is_valid:
    ip_string = input('Введите ip-адрес в формате 10.0.1.1: ')
    octets = ip_string.split('.')
    is_valid = len(octets) == 4

    for octet in octets:
        is_valid = octet.isdigit() and int(octet) in range(256) and is_valid
    if not is_valid:
        print('Неправильный IP-адрес')

if 1 <= int(octets[0]) <= 223:
    ip_type = 'unicast'
elif 224 <= int(octets[0]) <= 239:
    ip_type = 'multicast'
elif ip_string == '255.255.255.255':
    ip_type = 'local broadcast'
elif ip_string == '0.0.0.0':
    ip_type = 'unassigned'
else:
    ip_type = 'unused'

print(ip_type)