

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 335)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 80, 71, 41))
        self.label.setObjectName("label")
        self.price = QtWidgets.QLineEdit(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(140, 90, 141, 20))
        self.price.setObjectName("price")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 91, 16))
        self.label_2.setObjectName("label_2")
        self.dis = QtWidgets.QLineEdit(self.centralwidget)
        self.dis.setGeometry(QtCore.QRect(140, 120, 141, 20))
        self.dis.setObjectName("dis")
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setGeometry(QtCore.QRect(50, 150, 75, 23))
        self.calculate.clicked.connect(self.button_click)
        self.calculate.setObjectName("calculate")
        self.vatonly = QtWidgets.QLineEdit(self.centralwidget)
        self.vatonly.setGeometry(QtCore.QRect(140, 180, 141, 20))
        self.vatonly.setObjectName("vatonly")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 210, 91, 21))
        self.label_4.setObjectName("label_4")
        self.discounamount = QtWidgets.QLineEdit(self.centralwidget)
        self.discounamount.setGeometry(QtCore.QRect(140, 210, 141, 20))
        self.discounamount.setObjectName("discounamount")
        self.total = QtWidgets.QLineEdit(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(140, 240, 141, 20))
        self.total.setObjectName("total")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 111, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 351, 61))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def price(self):
        self.k = str(self.price.value())
    def dis(self):
        self.a = str(self.dis.value())
    def button_click(self):
        
        self.p = int(self.price.text())
        self.d = int(self.dis.text())
        self.string = 13/100*self.p
        self.vatonly.setText(str(self.string))
        self.disa = self.d*self.p/100
        self.discounamount.setText(str(self.disa))
        self.tota = self.p-self.d+self.string
        self.total.setText(str(self.tota))
            
   


        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Unique Nepal Hume Pipe Udhyog", "Unique Nepal Hume Pipe Udhyog"))
        self.label.setText(_translate("MainWindow", "ENTER PRICE"))
        self.price.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "DISCOUNT IN %"))
        self.dis.setText(_translate("MainWindow", "0"))
        self.calculate.setText(_translate("MainWindow", "Calculate"))
        self.vatonly.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "VAT Only"))
        self.label_4.setText(_translate("MainWindow", "Discount  amount"))
        self.discounamount.setText(_translate("MainWindow", "0"))
        self.total.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Total Amount with VAT "))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:15pt; font-weight:600; font-style:italic;\">Unique Nepal Hume Pipe Udhyog</span></p></body></html>"))


        

   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
