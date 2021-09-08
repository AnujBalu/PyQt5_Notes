from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class display(QMainWindow):
    def __init__(self):
        super(display, self).__init__()
        self.setWindowTitle("Lists")
        self.resize(600,500)

        layout = QVBoxLayout()

        list = QListWidget()

        list.addItems(["easy","medium", "hard"])
        list.currentItemChanged.connect(lambda x: print(x.text()))
        # this ".currentItemChanged" method is used to print the current selected text

        layout.addWidget(list)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])
window = display()
window.show()
app.exec()