from PySide6 import QtWidgets

from UI.Forms.practice_1_login import Ui_Form

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.show()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUi()

    def initUi(self) -> None:
        self.setWindowTitle("Авторизация")
        self.ui.lineEditLogin.setPlaceholderText("Введите логин")
        self.ui.lineEditPassword.setPlaceholderText("Введите логин")
        self.ui.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
   # window.show()

    app.exec()
