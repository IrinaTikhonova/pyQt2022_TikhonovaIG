"""
Модуль в котором содержаться потоки Qt
"""

import time

import psutil

import requests

from PySide6 import QtCore


class SystemInfo(QtCore.QThread):

    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while True:
            cpu_value = psutil.cpu_percent()
            ram_value = psutil.virtual_memory().percent
            cpu_ram_info = [cpu_value, ram_value]
            self.systemInfoReceived.emit(cpu_ram_info)
            time.sleep(self.delay)


class WeatherHandler(QtCore.QThread):
    weatherInfoReceived = QtCore.Signal(list)
    connectionError = QtCore.Signal(str)

    def __init__(self, lat=0, lon=0, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = False
        self.__latitude = lat
        self.__longitude = lon

    def setApiUrl(self, lat, lon):
        self.__latitude = lat
        self.__longitude = lon
        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def run(self) -> None:

        self.__status = True

        while self.__status:

            try:
                response = requests.get(self.__api_url)
                data = response.json()
                self.weatherInfoReceived.emit(data)
                time.sleep(self.__delay)

            except requests.exceptions.ConnectionError as e:
                self.stop()
                self.connectionError.emit(str(e.args[0].reason))

    def stop(self):

        self.__status = False

