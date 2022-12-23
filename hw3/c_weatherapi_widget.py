"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""
import time

from PySide6 import QtWidgets

from a_threads import WeatherHandler

from ui.forms.weather import Ui_Weather

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initThreads()
        self.ui = Ui_Weather()
        self.ui.setupUi(self)
        self.initSignals()


    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.startWeatherCheck)
        self.weatherInfo.finished.connect(self.onWeatherThreadFinished)
        self.weatherInfo.weatherInfoReceived.connect(self.onWeatherInfoReceived)
        self.weatherInfo.connectionError.connect(self.onConnectionError)

    def startWeatherCheck(self, status: bool):
        """
        :param status: состояние кнопки
        :return:
        """
        if status:
            try:
                lat = round(float(self.ui.lineEdit.text()), 2)
                lon = round(float(self.ui.lineEdit_2.text()), 2)
                if lat not in range(-90, 91) or lon not in range(-180, 181):
                    raise ValueError
            except:
                QtWidgets.QMessageBox.about(self, "ERROR", "Введены некорректные координаты")
                self.ui.plainTextEdit.setPlainText("Введены некорректные координаты")
                self.ui.pushButton.setChecked(False)
                return

            delay = int(self.ui.lineEdit_3.text())
            self.weatherInfo.setApiUrl(lat, lon)
            self.weatherInfo.setDelay(delay)
            self.weatherInfo.start()

            self.ui.pushButton.setText("Stop")
            self.ui.lineEdit_3.setEnabled(False)
            self.ui.lineEdit.setEnabled(False)
            self.ui.lineEdit_2.setEnabled(False)
        else:
            self.ui.pushButton.setEnabled(False)
            self.weatherInfo.stop()


    def onWeatherThreadFinished(self):
        self.ui.pushButton.setText("Start")
        self.ui.pushButton.setEnabled(True)
        self.ui.lineEdit.setEnabled(True)
        self.ui.lineEdit_2.setEnabled(True)
        self.ui.lineEdit_3.setEnabled(True)


    def onWeatherInfoReceived(self, data):
        latitude = data['latitude']
        longitude = data['longitude']
        temperature = data['current_weather']['temperature']
        windspeed = data['current_weather']['windspeed']

        self.ui.plainTextEdit.setPlainText(f"{time.ctime()}\n\n"
                                               f"широта: {latitude}, долгота: {longitude}\n\n"
                                               f"температура: {temperature}\n"
                                               f"скорость ветра: {windspeed}")

    def initThreads(self):
        self.weatherInfo = WeatherHandler()

    def closeEvent(self, event):
        self.weatherInfo.stop()
        self.weatherInfo.quit()

    def onConnectionError(self, connection_failure):
        QtWidgets.QMessageBox.about(self, "Connection ERROR", f"Try again later\n{connection_failure}")
        self.ui.pushButton.setChecked(False)

    """Пример из повторения Практика3 ниже:"""

    # def initSignals(self):
    #     """
    #
    #     :return:
    #     """
    #
    #     self.pushButton.clicked.connect(self.startUrlCheck)
    #     self.urlCheckerThread.started.connect(lambda: self.plainTextEdit.appendPlainText("Поток запущен"))
    #     self.urlCheckerThread.responsed.connect(lambda status_code: self.plainTextEdit.appendPlainText(f"{time.ctime()} Статус сайта: {status_code}"))
    #     self.urlCheckerThread.finished.connect(self.threadFinished)
    #     self.spinBox.valueChanged.connect(self.setTimeout)
    #
    # def startUrlCheck(self, status: bool) -> None:
    #     """
    #
    #     :param status: состояние кнопки
    #     :return:
    #     """
    #
    #     if status:
    #         url = self.lineEditUrl.text()
    #
    #         if not url:
    #             QtWidgets.QMessageBox.about(self, "Ошибка", "URL не заполнен")
    #             self.pushButton.setChecked(False)
    #             return None
    #
    #         self.urlCheckerThread.url = url
    #         self.urlCheckerThread.timeout = self.spinBox.value()
    #         self.urlCheckerThread.start()
    #         self.pushButton.setText("Остановить проверку")
    #     else:
    #         self.urlCheckerThread.status = False
    #         self.pushButton.setText("Запустить проверку")
    #         self.pushButton.setEnabled(False)
    #
    # def threadFinished(self):
    #     self.plainTextEdit.appendPlainText("Поток остановлен")
    #     self.pushButton.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()