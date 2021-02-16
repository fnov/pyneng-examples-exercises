# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

cidr = input('Введите IP-сети в формате CIDR (aa.bb.cc.dd/xx) ').split('/')
ipaddr = [int(i) for i in cidr[0].split('.')]

netmask = int(cidr[1])
binmask = '1' * netmask + '0' * (32 - netmask)
octmask = [int(binmask[i - 8:i], 2) for i in range(8, len(binmask) + 1, 8)]

out_net = ['Network:',
           '{0:<8}  {1:<8}  {2:<8}  {3:<8}',
           '{0:08b}  {1:08b}  {2:08b}  {3:08b}']
out_mask = ['Mask:',
            '/{mask}',
            '{0:<8}  {1:<8}  {2:<8}  {3:<8}',
            '{0:08b}  {1:08b}  {2:08b}  {3:08b}']

print('\n'.join(out_net).format(*ipaddr))
print('\n'.join(out_mask).format(*octmask, mask=netmask))
