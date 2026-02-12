# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
###################

iface_str, vlan_str = "interface", "vlan "

def get_int_vlan_map(config_filename: str) -> tuple[dict, dict]:
    access_dict = {}
    trunk_dict = {}
    with open(config_filename, 'r') as file:
        search_vlan = False
        for line in file:
            if not search_vlan:
                if iface_str in line:
                    iface = line.split()[-1]
                    search_vlan = True
                else:
                    continue
            else:
                if vlan_str in line:
                    if "access" in line:
                        access_dict[iface] = int(line.split()[-1])
                    elif "trunk" in line:
                        trunk_dict[iface] = [int(i) for i in line.split()[-1].split(',')]
                    search_vlan = False
    return access_dict, trunk_dict
