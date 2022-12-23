import time

from ui.forms.signals_events import Ui_Form

from PySide6 import QtCore, QtGui
"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit +  ).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtWidgets

from ui.forms.signals_events import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.Ui = Ui_Form()
        self.Ui.setupUi(self)
        self.initSignals()

    def initSignals(self):
        """


        """
        self.Ui.pushButtonLT.clicked.connect(lambda: self.move(0, 0))
        self.Ui.pushButtonRT.clicked.connect(self.moveRightTop)
        self.Ui.pushButtonLB.clicked.connect(self.moveLeftBottom)
        self.Ui.pushButtonRB.clicked.connect(self.moveRightBottom)
        self.Ui.pushButtonCenter.clicked.connect(self.moveCenter)
        self.Ui.pushButtonMoveCoords.clicked.connect(self.moveToCoordinates)
        self.Ui.pushButtonGetData.clicked.connect(self.screensInfo)


    def moveRightTop(self):

        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        screen_width = current_screen.size().width()
        pos_x = screen_width - self.width()

        self.move(pos_x, 0)

    def moveLeftBottom(self):

        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        screen_height = current_screen.size().height()
        pos_y = screen_height - self.height()

        self.move(0, pos_y)



    def moveRightBottom(self):

        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        screen_height = current_screen.size().height()
        pos_y = screen_height - self.height()
        screen_width = current_screen.size().width()
        pos_x = screen_width - self.width()

        self.move(pos_x, pos_y)

    def moveCenter(self):

        current_screen = QtWidgets.QApplication.screenAt(self.pos())
        screen_width_center = current_screen.size().width()/2
        screen_height_center = current_screen.size().height()/2
        pos_x_half = self.width()/2
        pos_y_half = self.height()/2

        self.move(screen_width_center - pos_x_half, screen_height_center - pos_y_half)

    def moveToCoordinates(self):

        self.move(self.Ui.spinBoxX.value(), self.Ui.spinBoxY.value())

    def screensInfo(self):

        self.Ui.plainTextEdit.appendPlainText(time.ctime())

        screens = QtWidgets.QApplication.screens()
        self.Ui.plainTextEdit.appendPlainText(f"Количество экранов {len(screens)}") # тут скорее всего неверно. Для именно подсчета не нашла

        main = QtWidgets.QApplication.screenAt(self.pos())
        self.Ui.plainTextEdit.appendPlainText(f"Текущее основное окно {main}") # и по этому вопрос

        geometry = QtWidgets.QApplication.screenAt(self.pos()).geometry()
        self.Ui.plainTextEdit.appendPlainText(f"Разрешение экрана {geometry}")

        win_size = self.size()
        self.Ui.plainTextEdit.appendPlainText(f"Размер окна {win_size}")

        min_size = self.minimumSize()
        self.Ui.plainTextEdit.appendPlainText(f"Минимальный размер окна {min_size}")

        center = self.geometry().center()
        self.Ui.plainTextEdit.appendPlainText(f"Центр окна {center}")

        base_screen = self.screen()
        self.Ui.plainTextEdit.appendPlainText(f"На каком экране окно находится {base_screen}")

        location =self.pos()
        self.Ui.plainTextEdit.appendPlainText(f"Текущее положение(координаты) окна {location}")

        app_state = QtWidgets.QApplication.applicationState()
        self.Ui.plainTextEdit.appendPlainText(f"Состояние окна {app_state}")

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        print(time.ctime(), f"\nНовый размер окна {self.size().width(), self.size().height()}")

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        print(time.ctime(), f"\nСтарая позиция: {event.oldPos()},\nНовая позиция: {event.pos()}")




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
