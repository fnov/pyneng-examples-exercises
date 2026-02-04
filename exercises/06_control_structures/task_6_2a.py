# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

###################

ip_string = input('Введите ip-адрес в формате 10.0.1.1: ')
octets = ip_string.split('.')
is_valid = len(octets) == 4

for octet in octets:
    is_valid = octet.isdigit() and int(octet) in range(256) and is_valid

if is_valid:
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
else:
    ip_type = 'Неправильный IP-адрес'

print(ip_type)
