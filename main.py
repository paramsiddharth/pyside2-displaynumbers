import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import \
	QApplication, QMainWindow, QWidget, QPushButton, \
	QVBoxLayout, QHBoxLayout, QLCDNumber, QSpinBox

class MyWin(QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Display Numbers')

		window = QWidget()
		layout = QVBoxLayout()
		
		quit = QPushButton('Quit')
		quit.setFont(QFont('Times', 18, QFont.Bold))
		
		lcd = QLCDNumber(2)
		lcd.setSegmentStyle(QLCDNumber.Filled)
		lcd.display(1)

		spinbox = QSpinBox()
		spinbox.setRange(1, 15)
		spinbox.setValue(1)

		btnBin = QPushButton('Binary')
		btnOct = QPushButton('Octal')
		btnDec = QPushButton('Decimal')
		btnHex = QPushButton('Hexadecimal')

		quit.clicked.connect(app.exit)
		spinbox.valueChanged.connect(lambda: lcd.display(spinbox.value()))
		btnBin.clicked.connect(lambda: 
			(lcd.setDigitCount(4),
			lcd.setMode(QLCDNumber.Bin),
			lcd.display(spinbox.value())))
		btnOct.clicked.connect(lambda: 
			(lcd.setDigitCount(2),
			lcd.setMode(QLCDNumber.Oct),
			lcd.display(spinbox.value())))
		btnDec.clicked.connect(lambda: 
			(lcd.setDigitCount(2),
			lcd.setMode(QLCDNumber.Dec),
			lcd.display(spinbox.value())))
		btnHex.clicked.connect(lambda: 
			(lcd.setDigitCount(1),
			lcd.setMode(QLCDNumber.Hex),
			lcd.display(spinbox.value())))
		
		layout.addWidget(quit)
		layout.addWidget(lcd)
		layout.addWidget(spinbox)
		buttons = QHBoxLayout()
		buttons.addWidget(btnBin)
		buttons.addWidget(btnOct)
		buttons.addWidget(btnDec)
		buttons.addWidget(btnHex)
		layout.addLayout(buttons)
		window.setLayout(layout)

		self.setCentralWidget(window)

def main():
	global app
	app = QApplication(sys.argv)
	primary = MyWin()	
	primary.show()
	app.exec_()

if __name__ == '__main__':
	main()