from PyQt5 import QtWidgets
from multiscreens import Ui_MainWindow

class MultiScreenApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self)

        self.mainWindow.comboBox.addItems(['USA','India','UK', 'France'])
        self.show()

    def goToRegister(self):
        self.mainWindow.stackedWidget.setCurrentIndex(1)

    def goToLogin(self):
        self.mainWindow.stackedWidget.setCurrentIndex(0)

    def onRegister(self):
        username = self.mainWindow.lineEdit_3.text()
        password = self.mainWindow.lineEdit_4.text()
        country = self.mainWindow.comboBox.currentText()
        if self.mainWindow.radioButton.isChecked():
            gender = 'male'
        else:
            gender = 'female'

        preferences = []
        if self.mainWindow.checkBox.isChecked():
            preferences.append('Travel')
        if self.mainWindow.checkBox_2.isChecked():
            preferences.append('Shopping')
        if self.mainWindow.checkBox_3.isChecked():
            preferences.append('Sports')

        print(username, password, country, gender, preferences)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    msa = MultiScreenApp()
    app.exec_()
