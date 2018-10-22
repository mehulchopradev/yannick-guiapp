from PyQt5 import QtWidgets
from login import Ui_MainWindow

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self)
        self.show()

    def on_reset(self):
        self.mainWindow.usernameEdit.setText('')
        self.mainWindow.passwordEdit.setText('')

    def on_login(self):
        username = self.mainWindow.usernameEdit.text()
        password = self.mainWindow.passwordEdit.text()

        print(username, password)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    loginWindow = LoginWindow()
    app.exec_()
