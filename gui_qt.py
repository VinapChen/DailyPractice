# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication,QLabel)


class Example(QWidget):

    def __init__(self):
        super(Example,self).__init__()

        self.initUI()


    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()


class MyWindow(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()

def show_mywindow():
    app = QApplication(sys.argv)
    mywindows = MyWindow()
    QLabel(mywindows).setText("<p style='color: red; margin-left: 20px'><b>hell world</b></p>")
    mywindows.show()
    # app.exec_()
    sys.exit(app.exec_())

# show_mywindow()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())