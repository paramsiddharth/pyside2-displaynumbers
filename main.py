import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import \
	QApplication, QWidget, QPushButton, \
	QVBoxLayout, QHBoxLayout, QLCDNumber, \
	QSlider

def main():
	global app
	app = QApplication(sys.argv)

	window = QWidget()
	layout = QVBoxLayout()
	
	quit = QPushButton('Quit')
	quit.setFont(QFont('Times', 18, QFont.Bold))
	
	lcd = QLCDNumber(2)
	lcd.setSegmentStyle(QLCDNumber.Filled)
	lcd.display(1)

	slider = QSlider(Qt.Horizontal)
	slider.setRange(1, 15)
	slider.setValue(1)

	btnBin = QPushButton('Binary')
	btnOct = QPushButton('Octal')
	btnDec = QPushButton('Decimal')
	btnHex = QPushButton('Hexadecimal')

	quit.clicked.connect(app.exit)
	slider.valueChanged.connect(lambda: lcd.display(slider.value()))
	btnBin.clicked.connect(lambda: 
		(lcd.setDigitCount(4),
		lcd.setMode(QLCDNumber.Bin),
		lcd.display(slider.value())))
	btnOct.clicked.connect(lambda: 
		(lcd.setDigitCount(2),
		lcd.setMode(QLCDNumber.Oct),
		lcd.display(slider.value())))
	btnDec.clicked.connect(lambda: 
		(lcd.setDigitCount(2),
		lcd.setMode(QLCDNumber.Dec),
		lcd.display(slider.value())))
	btnHex.clicked.connect(lambda: 
		(lcd.setDigitCount(1),
		lcd.setMode(QLCDNumber.Hex),
		lcd.display(slider.value())))
	
	layout.addWidget(quit)
	layout.addWidget(lcd)
	layout.addWidget(slider)
	buttons = QHBoxLayout()
	buttons.addWidget(btnBin)
	buttons.addWidget(btnOct)
	buttons.addWidget(btnDec)
	buttons.addWidget(btnHex)
	layout.addLayout(buttons)
	window.setLayout(layout)
	
	window.show()
	app.exec_()

if __name__ == '__main__':
	main()