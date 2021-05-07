# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

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
print(get_ip_type(ip_input))
