# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(50, 10, 256, 192))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))

if __name__=="__main__":
        import sys
        from PyQt5.QtGui import QIcon
        app=QtWidgets.QApplication(sys.argv)
        widget=QtWidgets.QWidget()
        ui=Ui_Form()
        ui.setupUi(widget)
        # widget.setWindowIcon(QIcon('web.png'))#增加icon图标，如果没有图片可以没有这句
        widget.show()
        sys.exit(app.exec_())

