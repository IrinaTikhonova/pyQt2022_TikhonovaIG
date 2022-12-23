"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""

from PySide6 import QtWidgets

from ui.forms.sys_wthr import Ui_Form
from a_threads import SystemInfo, WeatherHandler
import time

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThread()  # инициализация потока
        self.Ui = Ui_Form()
        self.Ui.setupUi(self)
        self.initSignals()
        self.error_msg = f"Введены некорректные координаты"

    def initThread(self):
        self.sysInfo = SystemInfo()
        self.sysInfo.start()
        self.weather = WeatherHandler()

    def initSignals(self):
        self.Ui.spinBox.valueChanged.connect(self.setDelayForSysInfo)
        self.sysInfo.systemInfoReceived.connect(self.SysInfoReceivedHandle)
        self.Ui.pushButton.clicked.connect(self.onButtonPressed)
        self.weather.finished.connect(self.onWeatherThreadFinished)
        self.weather.weatherInfoReceived.connect(self.onWeatherInfoReceived)
        self.weather.connectionError.connect(self.onConnectionError)

    def setDelayForSysInfo(self, value):
        self.sysInfo.delay = value

    def SysInfoReceivedHandle(self, list_info):
        self.Ui.lcdNumber.display(list_info[0])
        self.Ui.progressBar.setValue(round(list_info[1]))

    def onButtonPressed(self, status):

        if status:
            try:
                lat = round(float(self.Ui.lineEdit.text()), 2)
                lon = round(float(self.Ui.lineEdit_2.text()), 2)
                if lat < -90 or lat > 90 or lon < -180 or lon > 180:
                    raise ValueError
            except:
                QtWidgets.QMessageBox.about(self, "ERROR", self.error_msg)
                self.Ui.plainTextEdit.setPlainText(self.error_msg)
                self.Ui.pushButton.setChecked(False)
                return

            delay = int(self.Ui.lineEdit_3.text())
            self.weather.setApiUrl(lat, lon)
            self.weather.setDelay(delay)
            self.weather.start()
            self.Ui.pushButton.setText("Stop")
            self.Ui.lineEdit_3.setEnabled(False)
            self.Ui.lineEdit.setEnabled(False)
            self.Ui.lineEdit_2.setEnabled(False)
        else:
            self.Ui.pushButton.setEnabled(False)
            self.weather.stop()

    def onWeatherThreadFinished(self):
        self.Ui.pushButton.setText("Start")
        self.Ui.pushButton.setEnabled(True)
        self.Ui.lineEdit.setEnabled(True)
        self.Ui.lineEdit_2.setEnabled(True)
        self.Ui.lineEdit_3.setEnabled(True)

    def onWeatherInfoReceived(self, data):
        latitude = str(data['latitude'])
        longitude = str(data['longitude'])
        temperature = str(data['current_weather']['temperature'])
        windspeed = str(data['current_weather']['windspeed'])

        self.Ui.plainTextEdit.setPlainText(f"{time.ctime()}\n\n"
                                               f"широта: {latitude}, долгота: {longitude}\n\n"
                                               f"температура: {temperature}\n"
                                               f"скорость ветра: {windspeed}")

    def closeEvent(self, event):
        self.sysInfo.deleteLater()
        self.weather.stop()
        self.weather.quit()

    def onConnectionError(self, e):
        QtWidgets.QMessageBox.about(self, "Connection ERROR", f"Try again later\n{e}")
        self.Ui.pushButton.setChecked(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()