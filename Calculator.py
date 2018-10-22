from PyQt5 import QtWidgets
from calc import Ui_MainWindow

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self)
        self.mainWindow.opsBox.addItems(['+','-','*','/'])
        self.show()

    def calculate(self):
        firstno = float(self.mainWindow.firstEdt.text())
        secondno = float(self.mainWindow.secondEdt.text())
        ops = self.mainWindow.opsBox.currentText()

        if ops == '+':
            self.mainWindow.resultEdt.setText(str(firstno + secondno))
        elif ops == '-':
            self.mainWindow.resultEdt.setText(str(firstno - secondno))
        elif ops == '*':
            self.mainWindow.resultEdt.setText(str(firstno * secondno))
        elif ops == '/':
            self.mainWindow.resultEdt.setText(str(firstno / secondno))

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    calc = Calculator()
    app.exec_()
