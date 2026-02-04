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
###################

ip_string = input('Введите ip-адрес в формате 10.0.1.1: ')
ip_octets = [ int(octet) for octet in ip_string.split('.') ]
if ip_octets[0] in range(1, 224):
    ip_type = 'unicast'
elif  ip_octets[0] in range(224, 240):
    ip_type = 'multicast'
elif ip_string == '255.255.255.255':
    ip_type = 'local broadcast'
elif ip_string == '0.0.0.0':
    ip_type = 'unassigned'
else:
    ip_type = 'unused'

print(ip_type)
