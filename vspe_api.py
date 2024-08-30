"""Библиотека на основе VSPE_API.dll."""

import ctypes
import os
import typing

VSPE_API = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "VSPE_API.dll"))


# Activate VSPE API using activation key
# * \param key
# * \return result
# VSPE_API bool __cdecl vspe_activate(const char* key);
VSPE_API.vspe_activate.argtypes = (ctypes.c_char_p,)
VSPE_API.vspe_activate.restype = ctypes.c_bool


def vspe_activate(key: str) -> bool:
    """Активировать VSPE API с помощью ключа.

    :param key: Ключ активации
    :returns: Результат активации
    """
    return VSPE_API.vspe_activate(key.encode('utf8'))


# Get VSPE API activation error details
# * \return result
# VSPE_API char* __cdecl vspe_get_activation_error();
VSPE_API.vspe_get_activation_error.argtypes = ()
VSPE_API.vspe_get_activation_error.restype = ctypes.c_char_p


def vspe_get_activation_error() -> str:
    """Получить описание ошибки активации.

    :returns: Описание ошибки
    """
    return VSPE_API.vspe_get_activation_error().decode('utf8')


# Initialize VSPE core
# * \return result
# VSPE_API bool __cdecl vspe_initialize();
VSPE_API.vspe_initialize.argtypes = ()
VSPE_API.vspe_initialize.restype = ctypes.c_bool


def vspe_initialize() -> bool:
    """Инициализировать VSPE.

    :returns: Результат инициализации
    """
    return VSPE_API.vspe_initialize()


# Load configuration file
# * \param name
# * \return result
# VSPE_API bool __cdecl vspe_loadConfiguration(const char* name);
VSPE_API.vspe_loadConfiguration.argtypes = (ctypes.c_char_p,)
VSPE_API.vspe_loadConfiguration.restype = ctypes.c_bool


def vspe_loadConfiguration(name: str) -> bool:
    """Загрузить конфигурацию.

    :param name: Файл конфигурации
    :returns: Результат загрузки конфигурации
    """
    return VSPE_API.vspe_loadConfiguration(name.encode('utf8'))


# Save configuration
# * \param name
# * \return result
# VSPE_API bool __cdecl vspe_saveConfiguration(const char* name);
VSPE_API.vspe_saveConfiguration.argtypes = (ctypes.c_char_p,)
VSPE_API.vspe_saveConfiguration.restype = ctypes.c_bool


def vspe_saveConfiguration(name: str) -> bool:
    """Сохранить конфигурацию.

    :param name: Файл конфигурации
    :returns: Результат сохранения конфигурации
    """
    return VSPE_API.vspe_saveConfiguration(name.encode('utf8'))


# Create device
# * \param name Device name. For example "Connector", "Splitter", "Pair" etc.
# * \param initString device initialization string
# * \return deviceId
# VSPE_API int __cdecl vspe_createDevice(const char* name, const char* initString);
VSPE_API.vspe_createDevice.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
VSPE_API.vspe_createDevice.restype = ctypes.c_int


def vspe_createDevice(name: str, initString: str) -> int:
    """Создать устройство.

    :param name:        Название устройства (напр. Connector, Splitter, Pair и т.д.)
    :param initString:  Строка инициализации устройства
    :returns: Идентификатор устройства
    """
    return VSPE_API.vspe_createDevice(name.encode('utf8'), initString.encode('utf8'))


# Destroy device by deviceId
# * \param deviceId
# * \return result
# VSPE_API bool __cdecl vspe_destroyDevice(int deviceId);
VSPE_API.vspe_destroyDevice.argtypes = (ctypes.c_int,)
VSPE_API.vspe_destroyDevice.restype = ctypes.c_bool


def vspe_destroyDevice(deviceId: int) -> bool:
    """Удалить устройство.

    :param deviceId: Идентификатор устройства
    :returns: Результат удаления
    """
    return VSPE_API.vspe_destroyDevice(deviceId)


# Get VSPE devices count
# * \return result
# VSPE_API int __cdecl vspe_getDevicesCount();
VSPE_API.vspe_getDevicesCount.argtypes = ()
VSPE_API.vspe_getDevicesCount.restype = ctypes.c_int


def vspe_getDevicesCount() -> int:
    """Получить количество устройств.

    :returns: Количество устройств
    """
    return VSPE_API.vspe_getDevicesCount()


# Get VSPE deviceId by device index
# * \param idx device index
# * \return deviceId
# VSPE_API int __cdecl vspe_getDeviceIdByIdx(int idx);
VSPE_API.vspe_getDeviceIdByIdx.argtypes = (ctypes.c_int,)
VSPE_API.vspe_getDeviceIdByIdx.restype = ctypes.c_int


def vspe_getDeviceIdByIdx(idx: int) -> int:
    """Получить идентификатор устройства по индексу устройства.

    :param idx: Индекс устройства
    :returns: Идентификатор устройства
    """
    return VSPE_API.vspe_getDeviceIdByIdx(idx)


# Get VSPE deviceId by COM port index
# * \param ComPortIdx
# * \return deviceId (-1 if not found).
# VSPE_API int __cdecl vspe_getDeviceIdByComPortIndex(int ComPortIdx);
VSPE_API.vspe_getDeviceIdByComPortIndex.argtypes = (ctypes.c_int,)
VSPE_API.vspe_getDeviceIdByComPortIndex.restype = ctypes.c_int


def vspe_getDeviceIdByComPortIndex(ComPortIdx: int) -> int:
    """Получить идентификатор устройства по номеру COM-порта.

    :param ComPortIdx: Номер COM-порта
    :returns: Идентификатор устройства (-1, если не найдено)
    """
    return VSPE_API.vspe_getDeviceIdByComPortIndex(ComPortIdx)


# Get device information
# * \param deviceId
# * \param name [out] device name
# * \param initStirng [out] device initString
# * \param ok [out] device state (1 = good)
# * \param used [out] device clients count (0 - not used)
# * \return result
# VSPE_API bool __cdecl vspe_getDeviceInfo(int deviceId, const char** name, const char** initString,
#                                          int* ok, int* used);
VSPE_API.vspe_getDeviceInfo.argtypes = (
    ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_char_p),
    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)
)
VSPE_API.vspe_getDeviceInfo.restype = ctypes.c_bool


def vspe_getDeviceInfo(deviceId: int) -> typing.Optional[dict[str, typing.Union[str, int]]]:
    """Получить информацию об устройстве.

    :param deviceId: Идентификатор устройства
    :returns: Словарь параметров (название, строка инициализации, статус, использование), либо None
    """
    name = ctypes.pointer(ctypes.c_char_p())
    initString = ctypes.pointer(ctypes.c_char_p())
    ok = ctypes.pointer(ctypes.c_int())
    used = ctypes.pointer(ctypes.c_int())
    result = VSPE_API.vspe_getDeviceInfo(deviceId, name, initString, ok, used)
    if result:
        return {
            'name': name[0].decode('utf8'),
            'initString': initString[0].decode('utf8'),
            'ok': ok[0],
            'used': used[0],
        }
    else:
        return None


# Reinitialize device by deviceId
# * \param deviceId
# * \return result
# VSPE_API bool __cdecl vspe_reinitializeDevice(int deviceId);
VSPE_API.vspe_reinitializeDevice.argtypes = (ctypes.c_int,)
VSPE_API.vspe_reinitializeDevice.restype = ctypes.c_bool


def vspe_reinitializeDevice(deviceId: int) -> bool:
    """Реинициализировать устройство.

    :param deviceId: Идентификатор устройства
    :returns: Результат реинициализации
    """
    return VSPE_API.vspe_reinitializeDevice(deviceId)


# Destroy all devices
# * \return result
# VSPE_API bool __cdecl vspe_destroyAllDevices();
VSPE_API.vspe_destroyAllDevices.argtypes = ()
VSPE_API.vspe_destroyAllDevices.restype = ctypes.c_bool


def vspe_destroyAllDevices() -> bool:
    """Удалить все устройства.

    :returns: Результат удаления
    """
    return VSPE_API.vspe_destroyAllDevices()


# Start emulation
# * \return result
# VSPE_API bool __cdecl vspe_startEmulation();
VSPE_API.vspe_startEmulation.argtypes = ()
VSPE_API.vspe_startEmulation.restype = ctypes.c_bool


def vspe_startEmulation() -> bool:
    """Включить эмуляцию.

    :returns: Результат включения эмуляции
    """
    return VSPE_API.vspe_startEmulation()


# Stop emulation
# * \return result
# VSPE_API bool __cdecl vspe_stopEmulation();
VSPE_API.vspe_stopEmulation.argtypes = ()
VSPE_API.vspe_stopEmulation.restype = ctypes.c_bool


def vspe_stopEmulation() -> bool:
    """Отключить эмуляцию.

    :returns: Результат отключения эмуляции
    """
    return VSPE_API.vspe_stopEmulation()


# Release VSPE core
# VSPE_API void __cdecl vspe_release();
VSPE_API.vspe_release.argtypes = ()
VSPE_API.vspe_release.restype = None


def vspe_release() -> None:
    """Освободить VSPE."""
    VSPE_API.vspe_release()


# Get VSPE API version information
# * \return result
# VSPE_API const char* __cdecl vspe_getVersionInformation();
VSPE_API.vspe_getVersionInformation.argtypes = ()
VSPE_API.vspe_getVersionInformation.restype = ctypes.c_char_p


def vspe_getVersionInformation() -> str:
    """Получить информацию о версии VSPE API.

    :returns: Информация о версии VSPE API
    """
    return VSPE_API.vspe_getVersionInformation().decode('utf8')
