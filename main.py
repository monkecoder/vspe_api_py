"""Тестовый скрипт использования VSPE_API."""

import argparse
import functools

from vspe_api import *


def main_decorator(func):
    """Декоратор для функций VSPE API, активация, инициализация, освобождение."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Обёртка, начинает и заканчивает работу с VSPE API, в процессе исполняя нужную функцию."""
        print("Версия VSPE API:", vspe_getVersionInformation())

        if not vspe_activate(""):
            print("<Error> Ошибка активации:", vspe_get_activation_error())
            return -1

        if not vspe_initialize():
            print("<Error> Ошибка инициализации")
            return -2

        result = func(*args, **kwargs)

        vspe_release()
        return result

    return wrapper


@main_decorator
def create_connector(com_num):
    device_id = vspe_getDeviceIdByComPortIndex(com_num)
    if device_id != -1:
        print("Устройство уже существует")
        return 0

    if vspe_createDevice("Connector", f"{com_num};0") == -1:
        print("<Error> Не удалось создать устройство:", com_num)
        return -1

    print("Устройство создано:", com_num)

    if not vspe_startEmulation():
        print("<Error> Не удалось начать эмуляцию")
        return -2

    return 0


@main_decorator
def destroy_device(com_num):
    device_id = vspe_getDeviceIdByComPortIndex(com_num)
    if device_id == -1:
        print("Устройство не существует")
        return 0

    if not vspe_destroyDevice(device_id):
        print("<Error> Не удалось удалить устройство:", com_num)
        return -1

    print("Устройство удалено:", com_num)

    if vspe_getDevicesCount() == 0:
        if not vspe_stopEmulation():
            print("<Error> Не удалось остановить эмуляцию")
            return -2

    return 0


@main_decorator
def destroy_all_devices():
    if vspe_getDevicesCount() == 0:
        print("Нет устройств")
        return 0

    if not vspe_destroyAllDevices():
        print("<Error> Не удалось удалить все устройства")
        return -1

    print("Устройства удалены")

    if not vspe_stopEmulation():
        print("<Error> Не удалось остановить эмуляцию")
        return -2

    return 0


@main_decorator
def show_devices():
    count = vspe_getDevicesCount()
    for i in range(count):
        device_id = vspe_getDeviceIdByIdx(i)
        device_info = vspe_getDeviceInfo(device_id)
        if device_info:
            print("Устройство {0}: {1} ({2}) статус: {3}, используется: {4}".format(
                i + 1, device_info['name'], device_info['initString'],
                "ОК" if device_info['ok'] else "ОШИБКА", "ДА" if device_info['used'] else "НЕТ"
            ))
        else:
            print("Устройство {}: <Warning> Нет информации об устройстве".format(i + 1))

    if count == 0:
        print("Нет устройств")

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("start", "stop", "stopall", "show"))
    parser.add_argument("com_num", type=int, nargs="?")
    parser_args = parser.parse_args()

    if parser_args.command in {"start", "stop"} and parser_args.com_num is None:
        parser.error("stop/start command needs COM-number")

    match parser_args.command:
        case "start":
            err = create_connector(parser_args.com_num)
        case "stop":
            err = destroy_device(parser_args.com_num)
        case "stopall":
            err = destroy_all_devices()
        case "show":
            err = show_devices()
        case _:
            print("???")
            err = -10

    quit(err)
