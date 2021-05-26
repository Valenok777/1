import sys
from interface import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def test():
    ruble = int(ui.ruble.toPlainText())
    dollar_1 = 73.54
    dollar = ruble / dollar_1
    ui.dollar.setText(str(round(dollar, 2)))
    euro_1 = 89.94
    euro = ruble / euro_1
    ui.euro.setText(str(round(euro, 2)))
    dinar_1 = 244.50
    dinar = ruble / dinar_1
    ui.dinar.setText(str(round(dinar, 2)))
    rial_1 = 0.0017
    rial = ruble / rial_1
    ui.rial.setText(str(round(rial, 2)))




ui.count.clicked.connect(test)
sys.exit(app.exec_())