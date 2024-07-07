# Form implementation generated from reading ui file '.\roady_gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from roady import Roady


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 251)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.departure_city_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.departure_city_label.setGeometry(QtCore.QRect(10, 10, 81, 41))
        self.departure_city_label.setObjectName("departure_city_label")
        self.departre_city_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.departre_city_input.setGeometry(QtCore.QRect(100, 20, 113, 21))
        self.departre_city_input.setObjectName("departre_city_input")
        self.destination_city_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.destination_city_input.setGeometry(QtCore.QRect(370, 20, 113, 21))
        self.destination_city_input.setObjectName("destination_city_input")
        self.destination_city_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.destination_city_label.setGeometry(QtCore.QRect(280, 20, 91, 20))
        self.destination_city_label.setObjectName("destination_city_label")
        self.gas_combo_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.gas_combo_box.setGeometry(QtCore.QRect(10, 60, 71, 21))
        self.gas_combo_box.setObjectName("gas_combo_box")
        self.gas_combo_box.addItem("")
        self.gas_combo_box.addItem("")
        self.Consum_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Consum_label.setGeometry(QtCore.QRect(10, 100, 49, 16))
        self.Consum_label.setObjectName("Consum_label")
        self.fuel_usage = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.fuel_usage.setGeometry(QtCore.QRect(70, 100, 113, 21))
        self.fuel_usage.setObjectName("fuel_usage")
        self.number_of_persons_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.number_of_persons_label.setGeometry(QtCore.QRect(10, 130, 111, 16))
        self.number_of_persons_label.setObjectName("number_of_persons_label")
        self.number_of_persons_line_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.number_of_persons_line_edit.setGeometry(QtCore.QRect(130, 130, 113, 21))
        self.number_of_persons_line_edit.setObjectName("number_of_persons_line_edit")
        self.calculate_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculate_button.clicked.connect(self.calculate_btn)
        self.calculate_button.setGeometry(QtCore.QRect(240, 170, 161, 41))
        self.calculate_button.setObjectName("calculate_button")
        self.add_return_radio_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.add_return_radio_button.setGeometry(QtCore.QRect(138, 60, 91, 20))
        self.add_return_radio_button.setObjectName("add_return_radio_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.departure_city_label.setText(_translate("MainWindow", "Departure City"))
        self.destination_city_label.setText(_translate("MainWindow", "Destination City"))
        self.gas_combo_box.setItemText(0, _translate("MainWindow", "Benzina"))
        self.gas_combo_box.setItemText(1, _translate("MainWindow", "Motorina"))
        self.Consum_label.setText(_translate("MainWindow", "Consum"))
        self.number_of_persons_label.setText(_translate("MainWindow", "Number of persons"))
        self.calculate_button.setText(_translate("MainWindow", "CALCULATE"))
        self.add_return_radio_button.setText(_translate("MainWindow", "Dus/Intors"))

    def calculate_btn(self):
        departure_city = self.departre_city_input.text()
        destination_city = self.destination_city_input.text()
        number_of_persons = self.number_of_persons_line_edit.text()
        fuel_type = self.gas_combo_box.currentText()
        fuel_usage = self.fuel_usage.text()
        roady = Roady(departure_city,destination_city,
                        int(number_of_persons), float(fuel_usage), fuel_type)
        price = roady.calculate_price_per_person()
        if self.calculate_button.isEnabled():
            print(price*2)
        else:
            print(price)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())