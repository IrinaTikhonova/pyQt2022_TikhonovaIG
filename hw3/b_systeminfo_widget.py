"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets

from ui.forms.sinf import Ui_Form
from a_threads import SystemInfo


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThread()  # инициализация потока
        self.Ui = Ui_Form()
        self.Ui.setupUi(self)

        self.initSignals()  # инициализация сигналов

    def initThread(self):
        self.sysInfo = SystemInfo()
        self.sysInfo.start()

    def initSignals(self):
        self.Ui.spinBox.valueChanged.connect(self.setDelayForSysInfo)
        self.sysInfo.systemInfoReceived.connect(self.SysInfoReceivedHandle)

    def setDelayForSysInfo(self, value):
        self.sysInfo.delay = value

    def SysInfoReceivedHandle(self, list_info):
        self.Ui.lcdNumber.display(list_info[0])
        self.Ui.progressBar.setValue(round(list_info[1]))

    def closeEvent(self, event):
        self.sysInfo.deleteLater()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

