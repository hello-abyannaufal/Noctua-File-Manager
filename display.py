import os
import pathlib

from utility import ReadFiles
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 324)
        MainWindow.setStyleSheet("background-color: rgb(244, 121, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 0, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Good Times")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(255, 255, 255);")
        self.title.setObjectName("title")

        self.color_status = QtWidgets.QLabel(self.centralwidget)
        self.color_status.setGeometry(QtCore.QRect(410, 10, 81, 31))
        self.color_status.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.color_status.setText("")
        self.color_status.setObjectName("color_status")

        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(410, 30, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Geometric 706 Black Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setObjectName("status")

        self.frame_01 = QtWidgets.QFrame(self.centralwidget)
        self.frame_01.setGeometry(QtCore.QRect(10, 60, 481, 221))
        self.frame_01.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_01.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_01.setObjectName("frame_01")

        self.label1_f1 = QtWidgets.QLabel(self.frame_01)
        self.label1_f1.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Geometric 706 Black Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label1_f1.setFont(font)
        self.label1_f1.setObjectName("label1_f1")

        self.label2_f1 = QtWidgets.QLabel(self.frame_01)
        self.label2_f1.setGeometry(QtCore.QRect(10, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Geometric 706 Black Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label2_f1.setFont(font)
        self.label2_f1.setObjectName("label2_f1")

        self.label3_f1 = QtWidgets.QLabel(self.frame_01)
        self.label3_f1.setGeometry(QtCore.QRect(10, 90, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Geometric 706 Black Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label3_f1.setFont(font)
        self.label3_f1.setObjectName("label3_f1")

        self.label4_f1 = QtWidgets.QLabel(self.frame_01)
        self.label4_f1.setGeometry(QtCore.QRect(10, 130, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Geometric 706 Black Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label4_f1.setFont(font)
        self.label4_f1.setObjectName("label4_f1")

        self.edit2_f1 = QtWidgets.QLineEdit(self.frame_01)
        self.edit2_f1.setGeometry(QtCore.QRect(100, 49, 371, 31))
        self.edit2_f1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.edit2_f1.setText("")
        self.edit2_f1.setObjectName("edit2_f1")

        self.spinbox1_f1 = QtWidgets.QSpinBox(self.frame_01)
        self.spinbox1_f1.setGeometry(QtCore.QRect(100, 90, 51, 31))
        self.spinbox1_f1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                       "background-color: rgb(255, 255, 255);")
        self.spinbox1_f1.setObjectName("spinbox1_f1")

        self.edit1_f1 = QtWidgets.QLineEdit(self.frame_01)
        self.edit1_f1.setGeometry(QtCore.QRect(180, 10, 291, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.edit1_f1.setFont(font)
        self.edit1_f1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.edit1_f1.setText("")
        self.edit1_f1.setObjectName("edit1_f1")

        self.browse_f1 = QtWidgets.QPushButton(self.frame_01)
        self.browse_f1.setGeometry(QtCore.QRect(100, 10, 71, 31))
        self.browse_f1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browse_f1.setObjectName("browse_f1")
        self.browse_f1.clicked.connect(lambda: self.browse_folder())

        self.execute_f1 = QtWidgets.QPushButton(self.frame_01)
        self.execute_f1.setGeometry(QtCore.QRect(370, 170, 101, 41))
        self.execute_f1.setStyleSheet("background-color: rgb(255, 170, 100);")
        self.execute_f1.setObjectName("execute_f1")
        self.execute_f1.clicked.connect(self.execute)

        self.combo1_f1 = QtWidgets.QComboBox(self.frame_01)
        self.combo1_f1.setGeometry(QtCore.QRect(100, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.combo1_f1.setFont(font)
        self.combo1_f1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(255, 255, 255);")
        self.combo1_f1.setObjectName("combo1_f1")
        self.combo1_f1.addItem("Default")
        self.combo1_f1.addItem(".jpg")
        self.combo1_f1.addItem(".png")
        self.combo1_f1.addItem(".mp4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label2_f1.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>"))
        self.label3_f1.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" color:#ffffff;\">Numstart</span></p></body></html>"))
        self.edit2_f1.setPlaceholderText(_translate("MainWindow", "Insert filename here..."))
        self.label1_f1.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" color:#ffffff;\">Folder</span></p></body></html>"))
        self.edit1_f1.setPlaceholderText(_translate("MainWindow", "Load path output..."))
        self.browse_f1.setText(_translate("MainWindow", "Browse"))
        self.execute_f1.setText(_translate("MainWindow", "Start Processing"))
        self.label4_f1.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" color:#ffffff;\">Output</span></p></body></html>"))
        self.title.setText(_translate("MainWindow", "Noctua File Manager"))
        self.status.setText(_translate("MainWindow",
                                       "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Idle</span></p></body></html>"))

    # Insert function code below
    def browse_folder(self):
        path = str(pathlib.Path().resolve())
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory', path)
        self.edit1_f1.setText(folder)

    def execute(self):
        path = self.edit1_f1.text()
        filename = self.edit2_f1.text()
        numstart = int(self.spinbox1_f1.text())
        if self.combo1_f1.currentText() == 'Default':
            obj = os.listdir(path)
            ext = pathlib.Path(obj[0]).suffix
        else:
            ext = self.combo1_f1.currentText()

        scan = ReadFiles(path, filename, ext, numstart)
        scan.all_rename()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())