import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QLineEdit
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap

class My(QWidget):
    def __init__(self):
        super().__init__()
        self.Ui()
    def Ui(self):

        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    desk=app.desktop()
    ask=My()
    sys.exit(app.exec_())
