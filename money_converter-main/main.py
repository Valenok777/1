import sys
from interface import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def test():
	ruble = int(ui.ruble.toPlainText())
	print(type(ruble))
	WWW = ruble / 2
	ui.dollar.setText(WWW)


ui.count.clicked.connect(test)
sys.exit(app.exec_())