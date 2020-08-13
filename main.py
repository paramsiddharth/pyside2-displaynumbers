import sys
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

def main():
	global app
	app = QApplication(sys.argv)
	window = QWidget()
	layout = QVBoxLayout()
	quit = QPushButton('Quit')
	quit.setFont(QFont('Times', 18, QFont.Bold))
	quit.clicked.connect(app.exit)
	layout.addWidget(quit)
	window.setLayout(layout)
	window.show()
	app.exec_()

if __name__ == '__main__':
	main()