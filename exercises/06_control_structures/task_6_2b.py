# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_ip_type(ip_str: str) -> str:
    first_octet = int(ip_str.split('.')[0])

    if ip_input == '0.0.0.0':
        ip_type = 'unassigned'
    elif ip_input == '255.255.255.255':
        ip_type = 'local broadcast'
    elif 0 <= first_octet < 224:
        ip_type = 'unicast'
    elif 224 <= first_octet < 240:
        ip_type = 'multicast'
    else:
        ip_type = 'unused'

    return ip_type


is_ip_correct = False
ip_input = ''

while not is_ip_correct:
    ip_input = input('Введите IP-адрес: ')
    ip_octets = [int(i) for i in ip_input.split('.') if i.isdigit() and int(i) in range(256)]
    if len(ip_octets) == 4:
        is_ip_correct = True
    else:
        print('Неправильный IP-адрес')

print(get_ip_type(ip_input))
