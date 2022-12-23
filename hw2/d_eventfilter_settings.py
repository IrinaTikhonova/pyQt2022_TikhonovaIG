"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QShortcut, QKeySequence
from ui.forms.eventfilter_settings import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.Ui = Ui_Form()
        self.Ui.setupUi(self)
        self.initSignals()

        QShortcut(QKeySequence(QtCore.Qt.Key.Key_Plus), self, activated=self.onPlusPressed)
        QShortcut(QKeySequence(QtCore.Qt.Key.Key_Minus), self, activated=self.onMinusPressed)

        settings = QtCore.QSettings("eventfilter_settings")
        self.Ui.comboBox.setCurrentText(settings.value("comboBoxMode", "dec"))
        self.Ui.dial.setValue(settings.value("value", 0))

    def initSignals(self):

        self.Ui.horizontalSlider.valueChanged.connect(self.onSliderMove)
        self.Ui.dial.valueChanged.connect(self.onDialChange)
        self.Ui.comboBox.currentTextChanged.connect(self.onComboBoxChange)

    def onSliderMove(self):
        self.Ui.lcdNumber.display(self.Ui.horizontalSlider.value())
        self.Ui.dial.setValue(self.Ui.horizontalSlider.value())

    def onDialChange(self):
        self.Ui.lcdNumber.display(self.Ui.dial.value())
        self.Ui.horizontalSlider.setValue(self.Ui.dial.value())

    def onComboBoxChange(self):
        if self.Ui.comboBox.currentText() == "oct":
            self.Ui.lcdNumber.setOctMode()

        elif self.Ui.comboBox.currentText() == "bin":
            self.Ui.lcdNumber.setBinMode()

        elif self.Ui.comboBox.currentText() == "hex":
            self.Ui.lcdNumber.setHexMode()

        else:
            self.Ui.lcdNumber.setDecMode()


    def onPlusPressed(self):
        self.Ui.dial.setValue(self.Ui.dial.value() + 1)

    def onMinusPressed(self):
        self.Ui.dial.setValue(self.Ui.dial.value() - 1)

    def closeEvent(self, event):
        settings = QtCore.QSettings("eventfilter_settings")
        settings.setValue("value", self.Ui.dial.value())
        settings.setValue("comboBoxMode", self.Ui.comboBox.currentText())

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
