# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
################
from tabulate import tabulate
from task_12_1 import ping_ip_addresses


def print_ip_table(reachable: list, unreachable: list) -> None:
    result = {'Reachable': reachable, 'Unreachable':unreachable}
    print(tabulate(result, headers='keys'))


if __name__ == "__main__":
    reachable_ips, unreachable_ips = ping_ip_addresses(['8.8.8.8', '1.1.1.1', '10.255.255.254'])
    print_ip_table(reachable_ips, unreachable_ips)
