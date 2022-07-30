import pathlib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog

from work_pdf import encrypt, decrypt


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 300)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(70, 140, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(70, 170, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 140, 291, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 90, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 90, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 180, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 90, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(580, 140, 291, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 135, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_success = QtWidgets.QLabel(self.centralwidget)
        self.label_success.setGeometry(QtCore.QRect(100, 250, 900, 31))
        self.label_success.setAlignment(Qt.AlignCenter)
        self.label_success.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.event_handler()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encrypt/Decrypt PDF"))
        self.radioButton.setText(_translate("MainWindow", "Encrypt"))
        self.radioButton_2.setText(_translate("MainWindow", "Decrypt"))
        self.label.setText(_translate("MainWindow", "Select a function"))
        self.label_2.setText(_translate("MainWindow", "Select a file"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Enter the password"))
        self.pushButton_2.setText(_translate("MainWindow", "RUN"))

    def event_handler(self):
        self.pushButton.clicked.connect(self.browse_files)
        self.pushButton_2.clicked.connect(self.enc_or_dec)

    def browse_files(self):
        dir = str(pathlib.Path.cwd()).replace('\\', '/')
        fname = QFileDialog.getOpenFileName(self, 'Open file', dir, 'PDF Files (*.pdf)')
        self.filename = fname[0]
        self.lineEdit.setText(self.filename)

    def enc_or_dec(self):
        password = self.lineEdit_2.text()
        if self.radioButton.isChecked():
            enc_name = encrypt(self.filename, password)
            if enc_name:
                self.label_success.setStyleSheet("background-color: lightgreen")
                self.label_success.setText(f'The encrypted file {enc_name} has been successfully created')
            else:
                self.label_success.setStyleSheet("background-color: red")
                self.label_success.setText(f'The file {self.filename.split("/")[-1]} is already encrypted')
        elif self.radioButton_2.isChecked():
            dec_name = decrypt(self.filename, password)
            if not dec_name:
                self.label_success.setStyleSheet("background-color: red")
                self.label_success.setText(f'The file {self.filename.split("/")[-1]} was not encrypted')
            elif 'Invalid password' in dec_name:
                self.label_success.setStyleSheet("background-color: red")
                self.label_success.setText(dec_name)
            else:
                self.label_success.setStyleSheet("background-color: lightgreen")
                self.label_success.setText(f'The decrypted file {dec_name} has been successfully created')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
