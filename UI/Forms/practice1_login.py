# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Practice1_login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Login = QLabel(Form)
        self.Login.setObjectName(u"Login")
        self.Login.setMinimumSize(QSize(45, 0))

        self.horizontalLayout_3.addWidget(self.Login)

        self.LoginInput = QLineEdit(Form)
        self.LoginInput.setObjectName(u"LoginInput")

        self.horizontalLayout_3.addWidget(self.LoginInput)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Password = QLabel(Form)
        self.Password.setObjectName(u"Password")
        self.Password.setMinimumSize(QSize(45, 0))

        self.horizontalLayout_4.addWidget(self.Password)

        self.PasswordInput = QLineEdit(Form)
        self.PasswordInput.setObjectName(u"PasswordInput")

        self.horizontalLayout_4.addWidget(self.PasswordInput)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Ok = QPushButton(Form)
        self.Ok.setObjectName(u"Ok")

        self.horizontalLayout_5.addWidget(self.Ok)

        self.Undo = QPushButton(Form)
        self.Undo.setObjectName(u"Undo")

        self.horizontalLayout_5.addWidget(self.Undo)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.ForgotPassword = QPushButton(Form)
        self.ForgotPassword.setObjectName(u"ForgotPassword")

        self.horizontalLayout.addWidget(self.ForgotPassword)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.Registration = QPushButton(Form)
        self.Registration.setObjectName(u"Registration")

        self.horizontalLayout_2.addWidget(self.Registration)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Login.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.Password.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.Ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.Undo.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.ForgotPassword.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0431\u044b\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c?", None))
        self.Registration.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

