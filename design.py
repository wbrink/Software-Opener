# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'software_opener.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(306, 193)

        self.software_label = QtWidgets.QLabel(Form)
        self.software_label.setGeometry(QtCore.QRect(30, 100, 231, 20))
        self.software_label.setObjectName("software_label")

        #plcaed before the buttons so the cursor default to this
        self.upc_line_edit = QtWidgets.QLineEdit(Form)
        self.upc_line_edit.setGeometry(QtCore.QRect(20, 70, 241, 20))
        self.upc_line_edit.setClearButtonEnabled(True)
        self.upc_line_edit.setObjectName("upc_line_edit")

        self.open_button = QtWidgets.QPushButton(Form)
        self.open_button.setGeometry(QtCore.QRect(100, 130, 71, 31))
        self.open_button.setObjectName("open_button")

        self.search_button = QtWidgets.QPushButton(Form)
        self.search_button.setEnabled(True)
        self.search_button.setGeometry(QtCore.QRect(120, 140, 21, 16))
        self.search_button.setObjectName("search_button")
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 251, 20))
        self.label.setObjectName("label")

        self.software_label.raise_()
        self.search_button.raise_()
        self.upc_line_edit.raise_()
        self.label.raise_()
        self.open_button.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Software Opener"))
        self.software_label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.open_button.setText(_translate("Form", "Open"))
        self.search_button.setText(_translate("Form", "Search"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Enter UPC Code </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

