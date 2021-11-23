# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hm_arayüz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(220, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 220, 45))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("QLabel{\n"
"background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"\n"
"    \n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.silme = QtWidgets.QPushButton(self.centralwidget)
        self.silme.setGeometry(QtCore.QRect(0, 45, 55, 55))
        self.silme.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"")
        self.silme.setObjectName("silme")
        self.isaretDegistir = QtWidgets.QPushButton(self.centralwidget)
        self.isaretDegistir.setGeometry(QtCore.QRect(55, 45, 55, 55))
        self.isaretDegistir.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"")
        self.isaretDegistir.setObjectName("isaretDegistir")
        self.yuzdeAl = QtWidgets.QPushButton(self.centralwidget)
        self.yuzdeAl.setGeometry(QtCore.QRect(110, 45, 55, 55))
        self.yuzdeAl.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"")
        self.yuzdeAl.setObjectName("yuzdeAl")
        self.bolme = QtWidgets.QPushButton(self.centralwidget)
        self.bolme.setGeometry(QtCore.QRect(165, 45, 55, 55))
        self.bolme.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"")
        self.bolme.setObjectName("bolme")
        self.pb9 = QtWidgets.QPushButton(self.centralwidget)
        self.pb9.setGeometry(QtCore.QRect(110, 100, 55, 55))
        self.pb9.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"}")
        self.pb9.setObjectName("pb9")
        self.pb8 = QtWidgets.QPushButton(self.centralwidget)
        self.pb8.setGeometry(QtCore.QRect(55, 100, 55, 55))
        self.pb8.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"}")
        self.pb8.setObjectName("pb8")
        self.pb7 = QtWidgets.QPushButton(self.centralwidget)
        self.pb7.setGeometry(QtCore.QRect(0, 100, 55, 55))
        self.pb7.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"}")
        self.pb7.setObjectName("pb7")
        self.carpma = QtWidgets.QPushButton(self.centralwidget)
        self.carpma.setGeometry(QtCore.QRect(165, 100, 55, 55))
        self.carpma.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"")
        self.carpma.setObjectName("carpma")
        self.pb6 = QtWidgets.QPushButton(self.centralwidget)
        self.pb6.setGeometry(QtCore.QRect(110, 155, 55, 55))
        self.pb6.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"}")
        self.pb6.setObjectName("pb6")
        self.pb5 = QtWidgets.QPushButton(self.centralwidget)
        self.pb5.setGeometry(QtCore.QRect(55, 155, 55, 55))
        self.pb5.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"}")
        self.pb5.setObjectName("pb5")
        self.pb1 = QtWidgets.QPushButton(self.centralwidget)
        self.pb1.setGeometry(QtCore.QRect(0, 210, 55, 55))
        self.pb1.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"}")
        self.pb1.setObjectName("pb1")
        self.pb3 = QtWidgets.QPushButton(self.centralwidget)
        self.pb3.setGeometry(QtCore.QRect(110, 210, 55, 55))
        self.pb3.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"}")
        self.pb3.setObjectName("pb3")
        self.arti = QtWidgets.QPushButton(self.centralwidget)
        self.arti.setGeometry(QtCore.QRect(165, 210, 55, 55))
        self.arti.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"")
        self.arti.setObjectName("arti")
        self.pb2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb2.setGeometry(QtCore.QRect(55, 210, 55, 55))
        self.pb2.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"}")
        self.pb2.setObjectName("pb2")
        self.pb4 = QtWidgets.QPushButton(self.centralwidget)
        self.pb4.setGeometry(QtCore.QRect(0, 155, 55, 55))
        self.pb4.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"}")
        self.pb4.setObjectName("pb4")
        self.Eksi = QtWidgets.QPushButton(self.centralwidget)
        self.Eksi.setGeometry(QtCore.QRect(165, 155, 55, 55))
        self.Eksi.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"")
        self.Eksi.setObjectName("Eksi")
        self.nokta = QtWidgets.QPushButton(self.centralwidget)
        self.nokta.setGeometry(QtCore.QRect(110, 265, 55, 55))
        self.nokta.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"")
        self.nokta.setObjectName("nokta")
        self.pb0 = QtWidgets.QPushButton(self.centralwidget)
        self.pb0.setGeometry(QtCore.QRect(0, 265, 110, 55))
        self.pb0.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 127);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton: pressed{\n"
"color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"}")
        self.pb0.setObjectName("pb0")
        self.esittir = QtWidgets.QPushButton(self.centralwidget)
        self.esittir.setGeometry(QtCore.QRect(165, 265, 55, 55))
        self.esittir.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Arial\";\n"
"}\n"
"\n"
"")
        self.esittir.setObjectName("esittir")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.silme.setText(_translate("MainWindow", "C"))
        self.isaretDegistir.setText(_translate("MainWindow", "+/-"))
        self.yuzdeAl.setText(_translate("MainWindow", "%"))
        self.bolme.setText(_translate("MainWindow", "/"))
        self.pb9.setText(_translate("MainWindow", "9"))
        self.pb8.setText(_translate("MainWindow", "8"))
        self.pb7.setText(_translate("MainWindow", "7"))
        self.carpma.setText(_translate("MainWindow", "*"))
        self.pb6.setText(_translate("MainWindow", "6"))
        self.pb5.setText(_translate("MainWindow", "5"))
        self.pb1.setText(_translate("MainWindow", "1"))
        self.pb3.setText(_translate("MainWindow", "3"))
        self.arti.setText(_translate("MainWindow", "+"))
        self.pb2.setText(_translate("MainWindow", "2"))
        self.pb4.setText(_translate("MainWindow", "4"))
        self.Eksi.setText(_translate("MainWindow", "-"))
        self.nokta.setText(_translate("MainWindow", "."))
        self.pb0.setText(_translate("MainWindow", "0"))
        self.esittir.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

