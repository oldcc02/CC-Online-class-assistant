# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


# from my_socket.tcp_client import send_data
# from online_class_method.cc_log import writelog


class Login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(300, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login.sizePolicy().hasHeightForWidth())
        login.setSizePolicy(sizePolicy)
        login.setMinimumSize(QtCore.QSize(300, 350))
        login.setMaximumSize(QtCore.QSize(400, 450))
        login.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/cc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(21, 17, 261, 243))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Number = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Number.sizePolicy().hasHeightForWidth())
        self.Number.setSizePolicy(sizePolicy)
        self.Number.setText("")
        self.Number.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Number.setObjectName("Number")
        self.verticalLayout.addWidget(self.Number)
        self.Password = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Password.sizePolicy().hasHeightForWidth())
        self.Password.setSizePolicy(sizePolicy)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.verticalLayout.addWidget(self.Password)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.code = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.code.sizePolicy().hasHeightForWidth())
        self.code.setSizePolicy(sizePolicy)
        self.code.setText("")
        self.code.setObjectName("code")
        self.horizontalLayout_3.addWidget(self.code)
        self.codeimg = QtWidgets.QLabel(self.widget)
        self.codeimg.setObjectName("codeimg")
        self.horizontalLayout_3.addWidget(self.codeimg)
        self.code_re = QtWidgets.QPushButton(self.widget)
        self.code_re.setMaximumSize(QtCore.QSize(41, 31))
        self.code_re.setObjectName("code_re")
        self.horizontalLayout_3.addWidget(self.code_re)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.errorinfo = QtWidgets.QLabel(self.widget)
        self.errorinfo.setInputMethodHints(QtCore.Qt.ImhNone)
        self.errorinfo.setText("")
        self.errorinfo.setObjectName("errorinfo")
        self.verticalLayout.addWidget(self.errorinfo)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.isremember = QtWidgets.QCheckBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isremember.sizePolicy().hasHeightForWidth())
        self.isremember.setSizePolicy(sizePolicy)
        self.isremember.setObjectName("isremember")
        self.horizontalLayout.addWidget(self.isremember)
        self.iswindow = QtWidgets.QCheckBox(self.widget)
        self.iswindow.setObjectName("iswindow")
        self.horizontalLayout.addWidget(self.iswindow)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.CourseCheck = QtWidgets.QComboBox(self.widget)
        self.CourseCheck.setObjectName("CourseCheck")
        self.CourseCheck.addItem("")
        self.CourseCheck.addItem("")
        self.horizontalLayout_2.addWidget(self.CourseCheck)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.LoginBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginBtn.sizePolicy().hasHeightForWidth())
        self.LoginBtn.setSizePolicy(sizePolicy)
        self.LoginBtn.setMinimumSize(QtCore.QSize(101, 28))
        self.LoginBtn.setMaximumSize(QtCore.QSize(101, 28))
        self.LoginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoginBtn.setIconSize(QtCore.QSize(10, 10))
        self.LoginBtn.setCheckable(False)
        self.LoginBtn.setObjectName("LoginBtn")
        self.verticalLayout.addWidget(self.LoginBtn)
        login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.menubar.setObjectName("menubar")
        self.menucc = QtWidgets.QMenu(self.menubar)
        self.menucc.setObjectName("menucc")
        login.setMenuBar(self.menubar)
        self.actionbug = QtWidgets.QAction(login)
        self.actionbug.setObjectName("actionbug")
        self.action_cc_call = QtWidgets.QAction(login)
        self.action_cc_call.setObjectName("action_cc_call")
        self.menucc.addAction(self.actionbug)
        self.menucc.addSeparator()
        self.menucc.addAction(self.action_cc_call)
        self.menubar.addAction(self.menucc.menuAction())

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "cc网课助手"))
        self.label.setText(_translate("login", "   账号信息"))
        self.Number.setPlaceholderText(_translate("login", "账号"))
        self.Password.setPlaceholderText(_translate("login", "密码"))
        self.code.setPlaceholderText(_translate("login", "验证码"))
        self.codeimg.setText(_translate("login", "验证码"))
        self.code_re.setText(_translate("login", "刷新"))
        self.isremember.setText(_translate("login", "记住密码"))
        self.iswindow.setText(_translate("login", "无界面运行"))
        self.label_4.setText(_translate("login", "网课平台"))
        self.CourseCheck.setItemText(0, _translate("login", "超星学习通"))
        self.CourseCheck.setItemText(1, _translate("login", "暂无其他"))
        self.LoginBtn.setText(_translate("login", "确定"))
        self.menucc.setTitle(_translate("login", "cc助手"))
        self.actionbug.setText(_translate("login", "bug反馈"))
        self.action_cc_call.setText(_translate("login", "为cc打call"))


class UiLogin(QMainWindow, Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.splash = QtWidgets.QSplashScreen(QtGui.QPixmap('img/wait.gif'))
        self.splash.show()
        # self.client = None
        # self.flag = True
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def show(self) -> None:
        super().show()
        self.splash.close()

    # def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
    #     super().closeEvent(a0)
    #     if self.flag and self.client:
    #         try:
    #             code = send_data(self.client, data='exit')
    #         except Exception as e:
    #             writelog('向服务器发送断开信息失败')
    #             writelog(str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWidget = UiLogin()
    myWidget.show()
    sys.exit(app.exec_())
