from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class display(QMainWindow):
    def __init__(self):
        super(display,self).__init__()
        self.setWindowTitle("Combo Box")
        self.resize(500,600)
        layout = QVBoxLayout()

        line = QLineEdit()
        layout.addWidget(line)
        line.returnPressed.connect(lambda: print(line.text()))  # when Enter is pressed the text will be printed
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])
window = display()
window.show()
app.exec()