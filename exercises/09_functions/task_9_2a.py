# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Пример итогового словаря, который должна возвращать функция (перевод строки
после каждого элемента сделан для удобства чтения):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}
####################


def generate_trunk_config(intf_vlan_mapping: dict, trunk_template: list) -> dict[str, list[str]]:
    """
    Возвращает словарь всех портов в режиме trunk с конфигурацией на основе шаблона
    Args:
        intf_vlan_mapping: словарь с соответствием интерфейс-VLAN такого вида:
                            {'FastEthernet0/12':10,
                             'FastEthernet0/14':11,
                             'FastEthernet0/16':17}
        trunk_template: список команд для порта в режиме access
    Returns: словарь всех портов в режиме trunk с конфигурацией на основе шаблона
    """
    result = {}
    for iface, vlans in intf_vlan_mapping.items():
        commands = []
        for line in trunk_template:
            if line.endswith('allowed vlan'):
                commands.append(f'{line} {','.join([str(i) for i in vlans])}')
            else:
                commands.append(line)
        result[iface] = commands
    return result
