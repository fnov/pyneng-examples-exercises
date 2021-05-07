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


ip_input = input('Введите IP-адрес: ')
is_ip_correct = False

ip_octets = [int(i) for i in ip_input.split('.') if i.isdigit() and int(i) in range(256)]
if len(ip_octets) == 4:
    is_ip_correct = True

if is_ip_correct:
    print(get_ip_type(ip_input))
else:
    print('Неправильный IP-адрес')
