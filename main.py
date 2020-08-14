import sys
from PySide2.QtWidgets import QApplication
import ui

def main():
	global app
	app = QApplication(sys.argv)
	ui.app = app
	primary = ui.MyWin()
	primary.show()
	app.exec_()

if __name__ == '__main__':
	main()