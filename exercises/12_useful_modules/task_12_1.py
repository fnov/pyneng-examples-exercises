# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
######################
import subprocess


def ping_ip_addresses(ips: list) -> tuple:
    abailable_ips = []
    unavailable_ips = []
    for ip in ips:
       if run_command(f'ping -c 1 {ip}'):
           abailable_ips.append(ip)
       else:
           unavailable_ips.append(ip)
    return abailable_ips, unavailable_ips


def run_command(command):
    result = subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8')
    if result.returncode == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    ping_ip_addresses(['8.8.8.8', '1.1.1.1', '10.255.255.254'])
